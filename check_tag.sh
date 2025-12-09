#!/bin/bash
# Check if git tag matches version in pmesh/version.py

# For GitHub Actions (GITHUB_REF contains refs/tags/TAG_NAME)
if [[ -n "$GITHUB_REF" ]] && [[ "$GITHUB_REF" == refs/tags/* ]]; then
    TAG="${GITHUB_REF#refs/tags/}"
    if ! grep "$TAG" pmesh/version.py; then
        echo "Tag $TAG does not match pmesh/version.py. Bail."
        exit 1
    fi
fi

# Legacy Travis CI support
if [[ -n "$TRAVIS_TAG" ]]; then
    if ! grep "$TRAVIS_TAG" pmesh/version.py; then
        echo "Tag $TRAVIS_TAG does not match pmesh/version.py. Bail."
        exit 1
    fi
fi

exit 0
