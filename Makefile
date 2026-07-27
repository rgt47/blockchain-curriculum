# Makefile for the blockchain curriculum book.
#
# Docker-first, reproducible freeze regeneration. Adapted from the
# zzcollab (zzc) compendium Makefile used for rgtlab blog posts, scoped
# to the whole book. The container regenerates _freeze/ deterministically
# from the pinned renv.lock; Netlify and GitHub Actions then render the
# committed freeze without R.
#
# Typical loop:
#   1. edit chapter .qmd
#   2. make render        # regenerate _freeze/ (and _book/) in container
#   3. git add _freeze <chapter>.qmd && git commit && git push
#   4. GitHub Actions / Netlify deploy the committed freeze (no R needed)

IMAGE   := blockchain-curriculum
R_VERSION := $(shell grep 'ARG R_VERSION=' Dockerfile | head -1 | sed 's/.*=//')

# Run R/Quarto in the container with the project bind-mounted. --platform
# forces amd64 on Apple Silicon (rocker publishes amd64 only).
DOCKER_RUN := docker run --platform linux/amd64 --rm \
    -e RENV_CONFIG_AUTOLOADER_ENABLED=FALSE \
    -v "$(CURDIR)":/project -w /project

.PHONY: help docker-build docker-rebuild render freeze preview r rstudio \
        check-renv snapshot clean

help:
	@echo "Reproducible book targets:"
	@echo ""
	@echo "  docker-build    Build the pinned image from renv.lock"
	@echo "  docker-rebuild  Rebuild with no cache (force fresh)"
	@echo ""
	@echo "  render          quarto render in container -> regenerate _freeze/ + _book/"
	@echo "  freeze          Alias for render (emphasis: regenerate the freeze)"
	@echo "  preview         quarto preview in container on http://localhost:4321"
	@echo "  r               Interactive R session in the container"
	@echo "  rstudio         RStudio Server on http://localhost:8787 (user/pass: rstudio)"
	@echo ""
	@echo "  check-renv      renv::status() in container (lockfile vs. code)"
	@echo "  snapshot        renv::snapshot() -> update renv.lock after adding a package"
	@echo "  clean           Remove _book/ and *.tar.gz"
	@echo ""
	@echo "  Deploy: after 'make render', commit _freeze/ and push."
	@echo "  Netlify (netlify.toml) and .github/workflows/publish.yml deploy the freeze."

docker-build:
	DOCKER_BUILDKIT=1 docker build --platform linux/amd64 \
	    --build-arg R_VERSION=$(R_VERSION) -t $(IMAGE) .

docker-rebuild:
	DOCKER_BUILDKIT=1 docker build --no-cache --platform linux/amd64 \
	    --build-arg R_VERSION=$(R_VERSION) -t $(IMAGE) .

render:
	$(DOCKER_RUN) $(IMAGE) quarto render analysis/book

freeze: render

# quarto preview needs a published port and a bound host address.
preview:
	$(DOCKER_RUN) -p 4321:4321 $(IMAGE) \
	    quarto preview analysis/book --port 4321 --host 0.0.0.0 --no-browser

r:
	$(DOCKER_RUN) -it $(IMAGE) R

rstudio:
	@echo "RStudio Server -> http://localhost:8787 (user: rstudio, pass: rstudio)"
	docker run --platform linux/amd64 --rm -p 8787:8787 \
	    -e PASSWORD=rstudio -v "$(CURDIR)":/home/rstudio/project $(IMAGE) /init

check-renv:
	$(DOCKER_RUN) $(IMAGE) R -q -e "renv::status()"

snapshot:
	$(DOCKER_RUN) $(IMAGE) R -q -e "renv::snapshot(prompt = FALSE)"

clean:
	rm -rf _book *.tar.gz
