# syntax=docker/dockerfile:1.4
#======================================================================
# Reproducible build environment for the blockchain curriculum book.
#
# Adapted from the zzcollab (zzc) compendium template used for rgtlab
# blog posts, but scoped to the WHOLE book as a single compendium
# rather than one compendium per chapter. Its sole job is to regenerate
# the Quarto freeze (_freeze/) deterministically: R executes chunks
# here, results are written to _freeze/, and Netlify/CI render the
# committed freeze without needing R.
#
# Package versions are pinned by renv.lock (Pillar 1). The base image
# pins the R version and the OS snapshot; renv::restore then reconciles
# every package to the exact version recorded in the lockfile.
#
#   R version here MUST match the R version in renv.lock (4.6.1). If the
#   rocker tag below is not yet published, bump/lower R_VERSION to the
#   closest available tag; renv still restores the locked package
#   versions (with a benign R-version-mismatch warning).
#======================================================================

ARG R_VERSION=4.6.1

# rocker/verse = R + tidyverse + Quarto + TinyTeX (HTML and PDF output)
FROM rocker/verse:${R_VERSION}

ARG DEBIAN_FRONTEND=noninteractive

# Match the Quarto version pinned by netlify.toml and the GitHub Action
# so local freeze regeneration matches the deploy pipeline exactly.
ARG QUARTO_VERSION=1.5.57

# Reproducibility-critical environment. Packages are baked into the R
# system site-library at build time (below); RENV_CONFIG_AUTOLOADER_ENABLED
# makes the bind-mounted .Rprofile's renv/activate.R return early, so the
# git-ignored (therefore empty in-container) host renv/library is never
# put on .libPaths(). R resolves packages from site-library at the exact
# locked versions instead.
ENV LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    TZ=UTC \
    RENV_CONFIG_AUTOLOADER_ENABLED=FALSE \
    RENV_CONFIG_REPOS_OVERRIDE="https://packagemanager.posit.co/cran/__linux__/noble/latest"

# System libraries needed to build the pinned R packages from source
# when a binary is unavailable.
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt/lists,sharing=locked \
    set -ex && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        libfontconfig1-dev \
        libfreetype-dev \
        libpng-dev \
        libjpeg-dev \
        libicu-dev

# Pin Quarto to the pipeline version (overrides the bundled one).
RUN set -ex && \
    wget -q "https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-amd64.deb" && \
    dpkg -i "quarto-${QUARTO_VERSION}-linux-amd64.deb" && \
    rm "quarto-${QUARTO_VERSION}-linux-amd64.deb"

# Restore the exact package set from the lockfile into the R system
# site-library (always on .libPaths(), used flat). Copying only
# renv.lock keeps this layer cached until the lockfile actually changes.
COPY renv.lock /tmp/renv.lock
RUN R -e "install.packages('renv')" && \
    R -e "renv::restore(lockfile = '/tmp/renv.lock', library = .Library.site[1], prompt = FALSE)"

# Project files are bind-mounted at runtime (-v \$(pwd):/project).
WORKDIR /project

CMD ["bash"]
