# See eachdist.ini:
%global stable_version 1.11.1
%global prerel_version 0.30~b1
# Contents of python3-opentelemetry-proto are generated from proto files in a
# separate repository with a separate version number. We treat these as
# generated sources: we aren’t required by the guidelines to re-generate them
# (although we *may*) but we must include the original sources.
#
# See PROTO_REPO_BRANCH_OR_COMMIT in scripts/proto_codegen.sh for the correct
# version number.
%global proto_version 0.16.0

# Unfortunately, we cannot disable the prerelease packages without breaking
# almost all of the stable packages, because opentelemetry-sdk depends on the
# prerelease package opentelementry-semantic-conventions.
%bcond_without prerelease
# There are also experimental packages in eachdist.ini, with yet another
# version, but currently none of these actually exist. We will avoid packaging
# them if at all possible.

%if 0%{?el9}
%bcond_with flaky
# https://bugzilla.redhat.com/show_bug.cgi?id=2089057
%bcond_with backoff
# EPEL9 lacks python3dist(sphinx-autodoc-typehints)
# https://bugzilla.redhat.com/show_bug.cgi?id=2053664
# …and python3dist(django)
# https://bugzilla.redhat.com/show_bug.cgi?id=2033064
# …and python3dist(sphinx) is older than upstream requests, which may or may
# not be workable.
%bcond_with doc_pdf
%else
%bcond_without flaky
%bcond_without backoff

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf
%endif

Name:           python-opentelemetry
Version:        %{stable_version}
Release:        %autorelease
Summary:        OpenTelemetry Python API and SDK

License:        ASL 2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
Source0:        %{url}/archive/v%{version}/opentelemetry-python-%{version}.tar.gz
# Note that we do not currently use this source, but it contains the original
# .proto files for python3-opentelemetry-proto, so we must include it.
%global proto_url https://github.com/open-telemetry/opentelemetry-proto
Source1:        %{proto_url}/archive/v%{proto_version}/opentelemetry-proto-%{proto_version}.tar.gz

# Python 3.11: Enhanced error locations in tracebacks
# Expect ^^^^^^^^^ in tracebacks when testing them
Patch:          https://github.com/open-telemetry/opentelemetry-python/pull/2771.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global stable_distversion %(echo '%{stable_version}' | tr -d '~^')
%global stable_distinfo %{stable_distversion}.dist-info
# See eachdist.ini:
%global stable_pkgdirs %{shrink:
      opentelemetry-api
      opentelemetry-sdk
      opentelemetry-proto
      propagator/opentelemetry-propagator-jaeger
      propagator/opentelemetry-propagator-b3
      exporter/opentelemetry-exporter-zipkin-proto-http
      exporter/opentelemetry-exporter-zipkin-json
      exporter/opentelemetry-exporter-zipkin
      exporter/opentelemetry-exporter-prometheus
      %{?with_backoff:exporter/opentelemetry-exporter-otlp}
      %{?with_backoff:exporter/opentelemetry-exporter-otlp-proto-grpc}
      %{?with_backoff:exporter/opentelemetry-exporter-otlp-proto-http}
      exporter/opentelemetry-exporter-jaeger-thrift
      exporter/opentelemetry-exporter-jaeger-proto-grpc
      exporter/opentelemetry-exporter-jaeger}
%global prerel_distversion %(echo '%{prerel_version}' | tr -d '~^')
%global prerel_distinfo %{prerel_distversion}.dist-info
# See eachdist.ini:
%global prerel_pkgdirs %{shrink:
      tests/opentelemetry-test-utils
      exporter/opentelemetry-exporter-opencensus
      shim/opentelemetry-opentracing-shim
      opentelemetry-semantic-conventions}

%global common_description %{expand:
OpenTelemetry Python API and SDK.}

%description
%{common_description}


%package -n python3-opentelemetry-exporter-jaeger-proto-grpc
Summary:        Jaeger Protobuf Exporter for OpenTelemetry
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned. See comments
# following BuildRequires for a tabulation of such interdependencies.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-sdk = %{stable_version}-%{release}

%description -n python3-opentelemetry-exporter-jaeger-proto-grpc
This library allows to export tracing data to Jaeger
(https://www.jaegertracing.io/).


%package -n python3-opentelemetry-exporter-jaeger-thrift
Summary:        Jaeger Thrift Exporter for OpenTelemetry
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned. See comments
# following BuildRequires for a tabulation of such interdependencies.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-sdk = %{stable_version}-%{release}

%description -n python3-opentelemetry-exporter-jaeger-thrift
This library allows to export tracing data to Jaeger
(https://www.jaegertracing.io/) using Thrift.


%package -n python3-opentelemetry-exporter-jaeger
Summary:        Jaeger Exporters for OpenTelemetry
Version:        %{stable_version}

Obsoletes:      python3-opentelemetry-ext-jaeger < 1.0

# Dependencies across subpackages should be fully-versioned. See comments
# following BuildRequires for a tabulation of such interdependencies.
Requires:       python3-opentelemetry-exporter-jaeger-proto-grpc = %{stable_version}-%{release}
Requires:       python3-opentelemetry-exporter-jaeger-thrift = %{stable_version}-%{release}

%description -n python3-opentelemetry-exporter-jaeger
This library is provided as a convenience to install all supported Jaeger
Exporters. Currently it installs:
  • opentelemetry-exporter-jaeger-proto-grpc
  • opentelemetry-exporter-jaeger-thrift

To avoid unnecessary dependencies, users should install the specific package
once they’ve determined their preferred serialization method.


%if %{with prerelease}
%package -n python3-opentelemetry-exporter-opencensus
Summary:        OpenCensus Exporter
Version:        %{prerel_version}

Obsoletes:      python3-opentelemetry-ext-opencensusexporter < 1.0

# Dependencies across subpackages should be fully-versioned. See comments
# following BuildRequires for a tabulation of such interdependencies.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-sdk = %{stable_version}-%{release}

%description -n python3-opentelemetry-exporter-opencensus
This library allows to export traces using OpenCensus.
%endif


%if %{with backoff}
%package -n python3-opentelemetry-exporter-otlp-proto-grpc
Summary:        OpenTelemetry Collector Protobuf over gRPC Exporter
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned. See comments
# following BuildRequires for a tabulation of such interdependencies.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-sdk = %{stable_version}-%{release}
Requires:       python3-opentelemetry-proto = %{stable_version}-%{release}

%description -n python3-opentelemetry-exporter-otlp-proto-grpc
This library allows to export data to the OpenTelemetry Collector using the
OpenTelemetry Protocol using Protobuf over gRPC.
%endif


%if %{with backoff}
%package -n python3-opentelemetry-exporter-otlp-proto-http
Summary:        OpenTelemetry Collector Protobuf over HTTP Exporter
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned. See comments
# following BuildRequires for a tabulation of such interdependencies.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-sdk = %{stable_version}-%{release}
Requires:       python3-opentelemetry-proto = %{stable_version}-%{release}

%description -n python3-opentelemetry-exporter-otlp-proto-http
This library allows to export data to the OpenTelemetry Collector using the
OpenTelemetry Protocol using Protobuf over HTTP.
%endif


%if %{with backoff}
%package -n python3-opentelemetry-exporter-otlp
Summary:        OpenTelemetry Collector Exporters
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned. See comments
# following BuildRequires for a tabulation of such interdependencies.
Requires:       python3-opentelemetry-exporter-otlp-proto-grpc = %{stable_version}-%{release}

%description -n python3-opentelemetry-exporter-otlp
This library is provided as a convenience to install all supported
OpenTelemetry Collector Exporters. Currently it installs:

  • opentelemetry-exporter-otlp-proto-grpc
  • opentelemetry-exporter-otlp-proto-http

In the future, additional packages will be available:

  • opentelemetry-exporter-otlp-json-http

To avoid unnecessary dependencies, users should install the specific package
once they’ve determined their preferred serialization and protocol method.
%endif


%package -n python3-opentelemetry-exporter-prometheus
Summary:        OpenTelemetry Prometheus Exporter
Version:        %{prerel_version}

Obsoletes:      python3-opentelemetry-ext-prometheus < 1.0

Requires:       ((%{py3_dist prometheus_client} >= 0.5) with (%{py3_dist prometheus_client} < 1))
# Dependencies across subpackages should be fully-versioned. See comments
# following BuildRequires for a tabulation of such interdependencies.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-sdk = %{stable_version}-%{release}

%description -n python3-opentelemetry-exporter-prometheus
This library allows to export metrics data to Prometheus
(https://prometheus.io).


%package -n python3-opentelemetry-exporter-zipkin-json
Summary:        Zipkin Span JSON Exporter for OpenTelemetry
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned. See comments
# following BuildRequires for a tabulation of such interdependencies.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-sdk = %{stable_version}-%{release}

%description -n python3-opentelemetry-exporter-zipkin-json
This library allows export of tracing data to Zipkin (https://zipkin.io/) using
JSON for serialization.


%package -n python3-opentelemetry-exporter-zipkin-proto-http
Summary:        Zipkin Span Protobuf Exporter for OpenTelemetry
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned. See comments
# following BuildRequires for a tabulation of such interdependencies.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-sdk = %{stable_version}-%{release}
Requires:       python3-opentelemetry-exporter-zipkin-json = %{stable_version}-%{release}

%description -n python3-opentelemetry-exporter-zipkin-proto-http
This library allows export of tracing data to Zipkin (https://zipkin.io/) using
Protobuf for serialization.


%package -n python3-opentelemetry-exporter-zipkin
Summary:        Zipkin Span Exporters for OpenTelemetry
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned. See comments
# following BuildRequires for a tabulation of such interdependencies.
Requires:       python3-opentelemetry-exporter-zipkin-json = %{stable_version}-%{release}
Requires:       python3-opentelemetry-exporter-zipkin-proto-http = %{stable_version}-%{release}

Obsoletes:      python3-opentelemetry-ext-wsgi < 1.0

%description -n python3-opentelemetry-exporter-zipkin
This library is provided as a convenience to install all supported
OpenTelemetry Zipkin Exporters. Currently it installs:
  • opentelemetry-exporter-zipkin-json
  • opentelemetry-exporter-zipkin-proto-http

In the future, additional packages may be available:
  • opentelemetry-exporter-zipkin-thrift

To avoid unnecessary dependencies, users should install the specific package
once they've determined their preferred serialization method.


%package -n python3-opentelemetry-api
Summary:        OpenTelemetry Python API
Version:        %{stable_version}

# Note that the huge number of instrumentation packages are released in
# https://github.com/open-telemetry/opentelemetry-python-contrib and are not
# currently packaged.
#
# The base opentelemetry-instrumentation package was also moved to “contrib” in
# release 1.6.1/0.25~b1. We therefore obsolete it…
Obsoletes:      python3-opentelemetry-instrumentation < 0.25~b1.1
# …and its pre-1.0 name…
Obsoletes:      python3-opentelemetry-auto-instrumentation < 1.0
# …and the pre-1.0 packages it was obsoleting. (Most of these are
# instrumentation extensions.)

# These have all been renamed and are now part of opentelemetry-python-contrib.
# They have a prerelease version number, which is less than the version number
# of the old packages, so obsoleting by version number alone is insufficient.
# It is fortunate, then, that they also have new names, and it is unlikely the
# old names will ever come back in any form.
#
# Any renamed pre-1.0 packages that remain in this repository are instead
# obsoleted by the corresponding new packages.

#   • opentelemetry-instrumentation-aiohttp-client
Obsoletes:      python3-opentelemetry-ext-aiohttp-client < 1.0
#   • opentelemetry-instrumentation-asgi
Obsoletes:      python3-opentelemetry-ext-asgi < 1.0
#   • opentelemetry-instrumentation-dbapi
Obsoletes:      python3-opentelemetry-ext-dbapi < 1.0
#   • opentelemetry-instrumentation-django
Obsoletes:      python3-opentelemetry-ext-django < 1.0
#   • opentelemetry-instrumentation-flask
Obsoletes:      python3-opentelemetry-ext-flask < 1.0
#   • opentelemetry-instrumentation-grpc
Obsoletes:      python3-opentelemetry-ext-grpc < 1.0
#   • opentelemetry-instrumentation-jinja2
Obsoletes:      python3-opentelemetry-ext-jinja2 < 1.0
#   • opentelemetry-instrumentation-mysql
Obsoletes:      python3-opentelemetry-ext-mysql < 1.0
#   • opentelemetry-instrumentation-psycopg2
Obsoletes:      python3-opentelemetry-ext-psycopg2 < 1.0
#   • opentelemetry-instrumentation-pymongo
Obsoletes:      python3-opentelemetry-ext-pymongo < 1.0
#   • opentelemetry-instrumentation-pymysql
Obsoletes:      python3-opentelemetry-ext-pymysql < 1.0
#   • opentelemetry-instrumentation-redis
Obsoletes:      python3-opentelemetry-ext-redis < 1.0
#   • opentelemetry-instrumentation-requests
Obsoletes:      python3-opentelemetry-ext-requests < 1.0
#   • opentelemetry-instrumentation-sqlalchemy
Obsoletes:      python3-opentelemetry-ext-sqlalchemy < 1.0
#   • opentelemetry-instrumentation-sqlite3
Obsoletes:      python3-opentelemetry-ext-sqlite3 < 1.0
#   • opentelemetry-instrumentation-wsgi
Obsoletes:      python3-opentelemetry-ext-wsgi < 1.0

#   • opentelemetry-exporter-datadog
Obsoletes:      python3-opentelemetry-ext-datadog < 1.0

# The opentelemetry-distro package was moved to “contrib” in release
# 1.6.1/0.25~b1.
Obsoletes:      python3-opentelemetry-distro < 0.25~b1.1
Obsoletes:      python3-opentelemetry-distro+otlp < 0.25~b1.1

%description -n python3-opentelemetry-api
%{summary}.


%package -n python3-opentelemetry-proto
Summary:        OpenTelemetry Python Proto
Version:        %{stable_version}

%description -n python3-opentelemetry-proto
%{summary}.


%package -n python3-opentelemetry-sdk
Summary:        OpenTelemetry Python SDK
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned. See comments
# following BuildRequires for a tabulation of such interdependencies.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-semantic-conventions = %{prerel_version}-%{release}

%description -n python3-opentelemetry-sdk
%{summary}.


%if %{with prerelease}
%package -n python3-opentelemetry-semantic-conventions
Summary:        OpenTelemetry Python Semantic Conventions
Version:        %{prerel_version}

%description -n python3-opentelemetry-semantic-conventions
This library contains generated code for the semantic conventions defined by
the OpenTelemetry specification.
%endif


%package -n python3-opentelemetry-propagator-b3
Summary:        OpenTelemetry B3 Propagator
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned. See comments
# following BuildRequires for a tabulation of such interdependencies.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}

%description -n python3-opentelemetry-propagator-b3
This library provides a propagator for the B3 format.


%package -n python3-opentelemetry-propagator-jaeger
Summary:        OpenTelemetry Jaeger Propagator
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned. See comments
# following BuildRequires for a tabulation of such interdependencies.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}

%description -n python3-opentelemetry-propagator-jaeger
This library provides a propagator for the Jaeger format.


%if %{with prerelease}
%package -n python3-opentelemetry-opentracing-shim
Summary:        OpenTracing Shim for OpenTelemetry
Version:        %{prerel_version}

Obsoletes:      python3-opentelemetry-ext-opentracing-shim < 1.0

# Dependencies across subpackages should be fully-versioned. See comments
# following BuildRequires for a tabulation of such interdependencies.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}

%description -n python3-opentelemetry-opentracing-shim
%{summary}.
%endif


%if %{with prerelease}
%package -n python3-opentelemetry-test-utils
Summary:        OpenTracing Test Utilities
Version:        %{prerel_version}

# Dependencies across subpackages should be fully-versioned. See comments
# following BuildRequires for a tabulation of such interdependencies.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-sdk = %{stable_version}-%{release}

# Subpackage was renamed upstream
Obsoletes:      python3-opentelemetry-test < 0.26~b1-1

%description -n python3-opentelemetry-test-utils
This package provides internal testing utilities for the OpenTelemetry Python
project and provides no stability or quality guarantees. Please do not use it
for anything other than writing or running tests for the OpenTelemetry Python
project (github.com/open-telemetry/opentelemetry-python).
%endif


%package doc
Summary:        Documentation for python-opentelemetry
Version:        %{stable_version}

%description doc
This package provides documentation for python-opentelemetry.


%prep
%autosetup -p1 -n opentelemetry-python-%{stable_version}

%py3_shebang_fix .

# Fix a test that shells out to the unversioned Python command. This is OK
# upstream, but not in Fedora.
sed -r -i 's|shutil\.which\("python"\)|"%{python3}"|' \
    opentelemetry-sdk/tests/trace/test_trace.py

# Drop intersphinx mappings, since we can’t download remote inventories and
# can’t easily produce working hyperlinks from inventories in local
# documentation packages.
echo 'intersphinx_mapping.clear()' >> docs/conf.py

(
  # - We do not use formatters/linters/type-checkers/coverage.
  #
  # - ddtrace is mentioned in a README but does not seem to actually be used
  #   anywhere
  # - we do not need sphinx_rtd_theme because we are not building the
  #   documentation as HTML
  # - we do not need sphinx-jekyll-builder because we will not build website
  #   docs
  # - now that instrumentation is moved to contrib, wrapt is no longer used
  #   directly; it is a dependency for some examples, and is in the intersphinx
  #   mapping, which we don’t use since the build is offline
  # - grpcio-tools is needed only if we run scripts/proto_codegen.sh
  # - httpretty does not seem to actually be used anywhere; it may be an
  #   optional dependency for output from some linter
  # - readme-renderer is needed only if we run
  #   scripts/check_for_valid_readme.py; this is also the reason for the
  #   version-pinned dependency on bleach, so we remove that too
  #
  # - we must allow Flask 2.x, as in opentelemetry-test-utils
  #
  # - we must allow Sphinx 3.6+ and 4.x
  # - we must allow sphinx-autodoc-typehints 1.17
  # - we must allow opentracing 2.3.x and 2.4.x
  # - we must allow protobuf 3.19.x; furthermore, we are not generating the
  #   bindings from the proto files, so we don’t have to respect the version
  #   specification in dev-requirements.txt, only the ones in individual
  #   packages
  #
  # - upstream pins markupsafe==2.0.1:
  #     temporary fix. we should update the jinja, flask deps
  #     See https://github.com/pallets/markupsafe/issues/282
  #     breaking change introduced in markupsafe causes jinja, flask to break
  #   but we have no such luxury
  #
  # - if we are not building the documentation, then we should ignore
  #   documentation dependencies duplicated in dev-requirements.txt
  # - if we are not building the documentation, we do not need Django
  sed -r \
      -e '/\b(black|flake8|isort|mypy|mypy-protobuf|pylint|pytest-cov)\b/d' \
      -e '/\b(ddtrace|sphinx-(rtd-theme|jekyll-builder)|wrapt)\b/d' \
      -e '/\b(grpcio-tools|httpretty|readme-renderer|bleach)\b/d' \
      -e 's/\b(flask~=)1\.[[:digit:]]\b/\12\.0/' \
      -e 's/\b(sphinx(-autodoc-typehints)?|opentracing)~=/\1>=/' \
      -e 's/\b(protobuf)[>~]=.*/\1/' \
      -e 's/\b(markupsafe)==.*/\1/' \
      %{?!with_doc_pdf:-e '/\b(sphinx|django)\b/d'} \
      dev-requirements.txt %{?with_doc_pdf:docs-requirements.txt}

  # We can’t easily use %%pyproject_buildrequires -t to read tox.ini, since
  # it’s not associated with a particular package in the source archive, but we
  # can read out the relevant dependencies and dump them into the requirements
  # file for processing.
  '%{python3}' -c '
from configparser import ConfigParser

toxfile = "tox.ini"
cfg = ConfigParser()
if toxfile not in cfg.read(toxfile):
    raise SystemExit(f"Could not load {toxfile}")
for dep in cfg.get("testenv", "deps").splitlines():
    parts = dep.rstrip("\r\n").split(None, 2)
    if not parts or parts[0].startswith("-"):
        continue
    elif not parts[0].endswith(":"):
        raise ValueError(f"Confusing dependency: {dep!r}")
    command = parts[0][:-1]
    dep = parts[1]
    if any(what in command for what in ("cov", "mypy")):
        continue
    print(dep)
' %{?!with_flaky:| sed -r '/\bflaky\b/d'}
) | sed -r -e '/^#/d' -e '/^(.*\/)?opentelemetry-/d' | sort -u |
  tee requirements-filtered.txt

# Loosen any dependency versions that are pinned too tightly in subpackages.
# The find-then-modify pattern keeps us from discarding mtimes on sources that
# do not need modification.
#
# - we must allow opentracing 2.3.x and 2.4.x
for dep in 'opentracing'
do
  find . -type f -name 'setup.cfg' -exec gawk -vDEP="${dep}" \
      'NF==3 && $1==DEP && $2=="~=" { print FILENAME; nextfile }' '{}' '+' |
    xargs -r -t sed -r -i "s/\b(${DEP}[[:blank:]])~=/\\1>=/"
done


%generate_buildrequires
# We filter generated BR’s to avoid listing those that are provided by packages
# built in this spec file. For easier inspection, we also reorder and
# de-duplicate them.
(
  # Consolidated from dev-requirements.txt and docs-requirements.txt in %%prep,
  # with quite a bit of well-justified filtering and adjusting. We will tack it
  # onto each %%pyproject_buildrequires call.
  reqs="${PWD}/requirements-filtered.txt"

  for pkgdir in %{?with_prerelease:%{prerel_pkgdirs}} %{stable_pkgdirs}
  do
    pushd "${pkgdir}" >/dev/null
    if [[ "${pkgdir}" = 'exporter/opentelemetry-exporter-otlp' ]]
    then
      # No “test” extra:
      %pyproject_buildrequires -r
    else
      # Typical subpackage:
      %pyproject_buildrequires -x test "${reqs}"
    fi
    popd >/dev/null
  done
) | grep -vE '\bopentelemetry-' | sort -u


%build
for pkgdir in %{?with_prerelease:%{prerel_pkgdirs}} %{stable_pkgdirs}
do
  pushd "${pkgdir}"
  %pyproject_wheel
  popd
done

# Build documentation
%if %{with doc_pdf}
PYTHONPATH="%{pyproject_build_lib}" \
    %make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install


%check
for pkgdir in %{?with_prerelease:%{prerel_pkgdirs}} %{stable_pkgdirs}
do
  # Note we do not attempt to run tests for opentelemetry-test-utils, i.e.
  # tests/opentelemetry-test-utils; there are none in practice, and pytest would
  # indicate failure.
  if [[ "${pkgdir}" = 'tests/opentelemetry-test-utils' ]]
  then
    continue
  fi
%if %{without flaky}
  ignore='--ignore=opentelemetry-sdk/tests/metrics/test_periodic_exporting_metric_reader.py'
%endif
  %pytest "${pkgdir}" ${ignore-}
done


%files -n python3-opentelemetry-exporter-jaeger-proto-grpc
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-jaeger-proto-grpc/LICENSE
%doc exporter/opentelemetry-exporter-jaeger-proto-grpc/README.rst
%doc exporter/opentelemetry-exporter-jaeger-proto-grpc/examples

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter
%dir %{python3_sitelib}/opentelemetry/exporter/jaeger
%dir %{python3_sitelib}/opentelemetry/exporter/jaeger/proto

%{python3_sitelib}/opentelemetry/exporter/jaeger/proto/grpc
%{python3_sitelib}/opentelemetry_exporter_jaeger_proto_grpc-%{stable_distinfo}


%files -n python3-opentelemetry-exporter-jaeger-thrift
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-jaeger-thrift/LICENSE
%doc exporter/opentelemetry-exporter-jaeger-thrift/README.rst
%doc exporter/opentelemetry-exporter-jaeger-thrift/examples

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter
%dir %{python3_sitelib}/opentelemetry/exporter/jaeger

%{python3_sitelib}/opentelemetry/exporter/jaeger/thrift
%{python3_sitelib}/opentelemetry_exporter_jaeger_thrift-%{stable_distinfo}


%files -n python3-opentelemetry-exporter-jaeger
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-jaeger/LICENSE
%doc exporter/opentelemetry-exporter-jaeger/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter
%dir %{python3_sitelib}/opentelemetry/exporter/jaeger

%dir %{python3_sitelib}/opentelemetry/exporter/jaeger/__pycache__
%pycached %{python3_sitelib}/opentelemetry/exporter/jaeger/version.py
%{python3_sitelib}/opentelemetry_exporter_jaeger-%{stable_distinfo}


%if %{with prerelease}
%files -n python3-opentelemetry-exporter-opencensus
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-opencensus/LICENSE
%doc exporter/opentelemetry-exporter-opencensus/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter

%{python3_sitelib}/opentelemetry/exporter/opencensus
%{python3_sitelib}/opentelemetry_exporter_opencensus-%{prerel_distinfo}
%endif


%if %{with backoff}
%files -n python3-opentelemetry-exporter-otlp-proto-grpc
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-otlp-proto-grpc/LICENSE
%doc exporter/opentelemetry-exporter-otlp-proto-grpc/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter
%dir %{python3_sitelib}/opentelemetry/exporter/otlp
%dir %{python3_sitelib}/opentelemetry/exporter/otlp/proto

%{python3_sitelib}/opentelemetry/exporter/otlp/proto/grpc
%{python3_sitelib}/opentelemetry_exporter_otlp_proto_grpc-%{stable_distinfo}
%endif


%if %{with backoff}
%files -n python3-opentelemetry-exporter-otlp-proto-http
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-otlp-proto-http/LICENSE
%doc exporter/opentelemetry-exporter-otlp-proto-http/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter
%dir %{python3_sitelib}/opentelemetry/exporter/otlp
%dir %{python3_sitelib}/opentelemetry/exporter/otlp/proto

%{python3_sitelib}/opentelemetry/exporter/otlp/proto/http
%{python3_sitelib}/opentelemetry_exporter_otlp_proto_http-%{stable_distinfo}
%endif


%if %{with backoff}
%files -n python3-opentelemetry-exporter-otlp
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-otlp/LICENSE
%doc exporter/opentelemetry-exporter-otlp/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter
%dir %{python3_sitelib}/opentelemetry/exporter/otlp

%dir %{python3_sitelib}/opentelemetry/exporter/otlp/__pycache__
%pycached %{python3_sitelib}/opentelemetry/exporter/otlp/version.py
%{python3_sitelib}/opentelemetry_exporter_otlp-%{stable_distinfo}
%endif


%files -n python3-opentelemetry-exporter-prometheus
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-prometheus/LICENSE
%doc exporter/opentelemetry-exporter-prometheus/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter

%{python3_sitelib}/opentelemetry/exporter/prometheus
%{python3_sitelib}/opentelemetry_exporter_prometheus-%{prerel_distinfo}


%files -n python3-opentelemetry-exporter-zipkin-json
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-zipkin-json/LICENSE
# Not packaged since it is a zero-length file:
#doc exporter/opentelemetry-exporter-zipkin-json/CHANGELOG.md
%doc exporter/opentelemetry-exporter-zipkin-json/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter
%dir %{python3_sitelib}/opentelemetry/exporter/zipkin

%{python3_sitelib}/opentelemetry/exporter/zipkin/encoder
%{python3_sitelib}/opentelemetry/exporter/zipkin/json
%pycached %{python3_sitelib}/opentelemetry/exporter/zipkin/node_endpoint.py
%{python3_sitelib}/opentelemetry_exporter_zipkin_json-%{stable_distinfo}


%files -n python3-opentelemetry-exporter-zipkin-proto-http
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-zipkin-proto-http/LICENSE
# Not packaged since it is a zero-length file:
#doc exporter/opentelemetry-exporter-zipkin-proto-http/CHANGELOG.md
%doc exporter/opentelemetry-exporter-zipkin-proto-http/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter
%dir %{python3_sitelib}/opentelemetry/exporter/zipkin
%dir %{python3_sitelib}/opentelemetry/exporter/zipkin/proto

%{python3_sitelib}/opentelemetry/exporter/zipkin/proto/http
%{python3_sitelib}/opentelemetry_exporter_zipkin_proto_http-%{stable_distinfo}


%files -n python3-opentelemetry-exporter-zipkin
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-zipkin/LICENSE
%doc exporter/opentelemetry-exporter-zipkin/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter
%dir %{python3_sitelib}/opentelemetry/exporter/zipkin

%dir %{python3_sitelib}/opentelemetry/exporter/zipkin/__pycache__
%pycached %{python3_sitelib}/opentelemetry/exporter/zipkin/version.py
%{python3_sitelib}/opentelemetry_exporter_zipkin-%{stable_distinfo}


%files -n python3-opentelemetry-api
# Note that the contents are identical to the top-level LICENSE file.
%license opentelemetry-api/LICENSE
%doc opentelemetry-api/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/propagators

%{python3_sitelib}/opentelemetry/_metrics
%{python3_sitelib}/opentelemetry/attributes
%{python3_sitelib}/opentelemetry/baggage
%{python3_sitelib}/opentelemetry/context
%{python3_sitelib}/opentelemetry/propagate
%dir %{python3_sitelib}/opentelemetry/propagators/__pycache__
%pycached %{python3_sitelib}/opentelemetry/propagators/composite.py
%pycached %{python3_sitelib}/opentelemetry/propagators/textmap.py
%{python3_sitelib}/opentelemetry/trace
%{python3_sitelib}/opentelemetry/util
%dir %{python3_sitelib}/opentelemetry/__pycache__
%pycached %{python3_sitelib}/opentelemetry/environment_variables.py
%pycached %{python3_sitelib}/opentelemetry/version.py
%{python3_sitelib}/opentelemetry_api-%{stable_distinfo}


%files -n python3-opentelemetry-proto
# Note that the contents are identical to the top-level LICENSE file.
%license opentelemetry-proto/LICENSE
%doc opentelemetry-proto/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed

%{python3_sitelib}/opentelemetry/proto
%{python3_sitelib}/opentelemetry_proto-%{stable_distinfo}


%files -n python3-opentelemetry-sdk
# Note that the contents are identical to the top-level LICENSE file.
%license opentelemetry-sdk/LICENSE
%doc opentelemetry-sdk/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed

%{python3_sitelib}/opentelemetry/sdk
%{python3_sitelib}/opentelemetry_sdk-%{stable_distinfo}


%if %{with prerelease}
%files -n python3-opentelemetry-semantic-conventions
# Note that the contents are identical to the top-level LICENSE file.
%license opentelemetry-sdk/LICENSE
%doc opentelemetry-sdk/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed

%{python3_sitelib}/opentelemetry/semconv
%{python3_sitelib}/opentelemetry_semantic_conventions-%{prerel_distinfo}
%endif


%files -n python3-opentelemetry-propagator-b3
# Note that the contents are identical to the top-level LICENSE file.
%license propagator/opentelemetry-propagator-b3/LICENSE
%doc propagator/opentelemetry-propagator-b3/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/propagators

%{python3_sitelib}/opentelemetry/propagators/b3
%{python3_sitelib}/opentelemetry_propagator_b3-%{stable_distinfo}


%files -n python3-opentelemetry-propagator-jaeger
# Note that the contents are identical to the top-level LICENSE file.
%license propagator/opentelemetry-propagator-jaeger/LICENSE
%doc propagator/opentelemetry-propagator-jaeger/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/propagators

%{python3_sitelib}/opentelemetry/propagators/jaeger
%{python3_sitelib}/opentelemetry_propagator_jaeger-%{stable_distinfo}


%if %{with prerelease}
%files -n python3-opentelemetry-opentracing-shim
# Note that the contents are identical to the top-level LICENSE file.
%license shim/opentelemetry-opentracing-shim/LICENSE
%doc shim/opentelemetry-opentracing-shim/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/shim

%{python3_sitelib}/opentelemetry/shim/opentracing_shim
%{python3_sitelib}/opentelemetry_opentracing_shim-%{prerel_distinfo}
%endif


%if %{with prerelease}
%files -n python3-opentelemetry-test-utils
%license LICENSE
%doc tests/opentelemetry-test-utils/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed

%{python3_sitelib}/opentelemetry/test
%{python3_sitelib}/opentelemetry_test_utils-%{prerel_distinfo}
%endif


%files doc
%license LICENSE
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc rationale.md
%doc README.md
%if %{with doc_pdf}
%doc docs/_build/latex/opentelemetrypython.pdf
%endif


%changelog
%autochangelog
