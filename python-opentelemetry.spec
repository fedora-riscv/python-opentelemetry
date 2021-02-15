%global srcname opentelemetry
%global _description %{summary}.

Name:           python-%{srcname}
Version:        0.8.0
Release:        5%{?dist}
Summary:        The OpenTelemetry Python client

License:        ASL 2.0
URL:            https://github.com/open-telemetry/%{srcname}-python/
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Fix Python requirement versions
Patch0:         %{name}-0.8.0-requirements.patch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
# Required for tests
BuildRequires:  %{py3_dist aiohttp}
BuildRequires:  %{py3_dist asgiref}
BuildRequires:  %{py3_dist django}
BuildRequires:  %{py3_dist flask}
BuildRequires:  %{py3_dist grpcio}
BuildRequires:  %{py3_dist httpretty}
BuildRequires:  %{py3_dist jinja2}
BuildRequires:  %{py3_dist mysql-connector-python}
BuildRequires:  %{py3_dist opencensus-proto}
BuildRequires:  %{py3_dist prometheus-client}
BuildRequires:  %{py3_dist protobuf}
BuildRequires:  %{py3_dist psycopg2}
BuildRequires:  %{py3_dist pymongo}
BuildRequires:  %{py3_dist pymysql}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist redis}
BuildRequires:  %{py3_dist requests}
BuildRequires:  %{py3_dist sqlalchemy}
BuildRequires:  %{py3_dist thrift}
BuildRequires:  %{py3_dist wrapt}
# Required for documentation
BuildRequires:  make
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-autodoc-typehints}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildArch:      noarch

%description
%{_description}


%package -n python3-%{srcname}-api
Summary:        OpenTelemetry Python API
%py_provides python3-%{srcname}-api

%description -n python3-%{srcname}-api
%{_description}


%package -n python3-%{srcname}-auto-instrumentation
Summary:        OpenTelemetry Auto Instrumentation
%py_provides python3-%{srcname}-auto-instrumentation

%description -n python3-%{srcname}-auto-instrumentation
%{summary}.


%package -n python3-%{srcname}-sdk
Summary:        OpenTelemetry Python SDK
%py_provides python3-%{srcname}-sdk

%description -n python3-%{srcname}-sdk
%{summary}.


%package -n python3-%{srcname}-ext-aiohttp-client
Summary:        OpenTelemetry aiohttp client Integration
%py_provides python3-%{srcname}-ext-aiohttp-client

%description -n python3-%{srcname}-ext-aiohttp-client
This library allows tracing HTTP requests made by the aiohttp client library.


%package -n python3-%{srcname}-ext-asgi
Summary:        OpenTelemetry ASGI Middleware
%py_provides python3-%{srcname}-ext-asgi

%description -n python3-%{srcname}-ext-asgi
This library provides a ASGI middleware that can be used on any ASGI framework
(such as Django, Starlette, FastAPI or Quart) to track requests timing through
OpenTelemetry.


# %%package -n python3-%%{srcname}-ext-datadog
# Summary:        OpenTelemetry Datadog Exporter
# %%py_provides python3-%%{srcname}-ext-datadog

# %%description -n python3-%%{srcname}-ext-datadog
# This library allows to export tracing data to Datadog. OpenTelemetry span event
# and links are not supported.


%package -n python3-%{srcname}-ext-dbapi
Summary:        OpenTelemetry Database API integration
%py_provides python3-%{srcname}-ext-dbapi

%description -n python3-%{srcname}-ext-dbapi
%{summary}.


%package -n python3-%{srcname}-ext-django
Summary:        OpenTelemetry Django Tracing
%py_provides python3-%{srcname}-ext-django

%description -n python3-%{srcname}-ext-django
This library allows tracing requests for Django applications.


%package -n python3-%{srcname}-ext-flask
Summary:        OpenTelemetry Flask Tracing
%py_provides python3-%{srcname}-ext-flask

%description -n python3-%{srcname}-ext-flask
This library builds on the OpenTelemetry WSGI middleware to track web requests
in Flask applications.


%package -n python3-%{srcname}-ext-grpc
Summary:        OpenTelemetry gRPC Integration
%py_provides python3-%{srcname}-ext-grpc

%description -n python3-%{srcname}-ext-grpc
Client and server interceptors for gRPC Python.


%package -n python3-%{srcname}-ext-jaeger
Summary:        OpenTelemetry Jaeger Exporter
%py_provides python3-%{srcname}-ext-jaeger

%description -n python3-%{srcname}-ext-jaeger
his library allows to export tracing data to Jaeger.


%package -n python3-%{srcname}-ext-jinja2
Summary:        OpenTelemetry jinja2 integration
%py_provides python3-%{srcname}-ext-jinja2

%description -n python3-%{srcname}-ext-jinja2
%{summary}.


%package -n python3-%{srcname}-ext-mysql
Summary:        OpenTelemetry MySQL Integration
%py_provides python3-%{srcname}-ext-mysql

%description -n python3-%{srcname}-ext-mysql
Integration with MySQL that supports the mysql-connector library and is
specified to trace_integration using MySQL.


%package -n python3-%{srcname}-ext-opencensusexporter
Summary:        OpenCensus Exporter
%py_provides python3-%{srcname}-ext-opencensusexporter

%description -n python3-%{srcname}-ext-opencensusexporter
This library allows to export traces and metrics using OpenCensus.


# %%package -n python3-%%{srcname}-ext-opentracing-shim
# Summary:        OpenTracing Shim for OpenTelemetry
# %%py_provides python3-%%{srcname}-ext-opentracing-shim

# %%description -n python3-%%{srcname}-ext-opentracing-shim
# %%{summary}.


%package -n python3-%{srcname}-ext-prometheus
Summary:        OpenTelemetry Prometheus Exporter
%py_provides python3-%{srcname}-ext-prometheus

%description -n python3-%{srcname}-ext-prometheus
This library allows to export metrics data to Prometheus.


%package -n python3-%{srcname}-ext-psycopg2
Summary:        OpenTelemetry Psycopg Integration
%py_provides python3-%{srcname}-ext-psycopg2

%description -n python3-%{srcname}-ext-psycopg2
%{summary}.


%package -n python3-%{srcname}-ext-pymongo
Summary:        OpenTelemetry pymongo Integration
%py_provides python3-%{srcname}-ext-pymongo

%description -n python3-%{srcname}-ext-pymongo
%{summary}.


%package -n python3-%{srcname}-ext-pymysql
Summary:        OpenTelemetry PyMySQL integration
%py_provides python3-%{srcname}-ext-pymysql

%description -n python3-%{srcname}-ext-pymysql
%{summary}.


%package -n python3-%{srcname}-ext-redis
Summary:        OpenTelemetry Redis Instrumentation
%py_provides python3-%{srcname}-ext-redis

%description -n python3-%{srcname}-ext-redis
This library allows tracing requests made by the Redis library.


%package -n python3-%{srcname}-ext-requests
Summary:        OpenTelemetry requests Integration
%py_provides python3-%{srcname}-ext-requests

%description -n python3-%{srcname}-ext-requests
This library allows tracing HTTP requests made by the requests library.


%package -n python3-%{srcname}-ext-sqlalchemy
Summary:        OpenTelemetry SQLAlchemy Tracing
%py_provides python3-%{srcname}-ext-sqlalchemy

%description -n python3-%{srcname}-ext-sqlalchemy
This library allows tracing requests made by the SQLAlchemy library.


%package -n python3-%{srcname}-ext-sqlite3
Summary:        OpenTelemetry SQLite3 Integration
%py_provides python3-%{srcname}-ext-sqlite3

%description -n python3-%{srcname}-ext-sqlite3
%{summary}.


%package -n python3-%{srcname}-ext-wsgi
Summary:        OpenTelemetry WSGI Middleware
%py_provides python3-%{srcname}-ext-wsgi

%description -n python3-%{srcname}-ext-wsgi
This library provides a WSGI middleware that can be used on any WSGI framework
(such as Django/Flask) to track requests timing through OpenTelemetry.


%package -n python3-%{srcname}-ext-zipkin
Summary:        OpenTelemetry Zipkin Exporter
%py_provides python3-%{srcname}-ext-zipkin

%description -n python3-%{srcname}-ext-zipkin
This library allows to export tracing data to Zipkin.


%package doc
Summary:        Documentation for %{name}

%description doc
This package provides documentation for %{name}.


%prep
%autosetup -p0 -n %{srcname}-python-%{version}

# Remove bundled egg-info
for i in $(find . -name "setup.py"); do
    rm -rf ${i%/*}/src/*.egg-info
done

# Delete extensions which can't be installed because of missing dependencies in
# Fedora
rm -r ext/opentelemetry-ext-{datadog,opentracing-shim}/

# Remove shebang
pushd opentelemetry-auto-instrumentation/src/opentelemetry/auto_instrumentation/
for i in auto_instrumentation.py bootstrap.py; do
    sed -e '1{\@^#!/usr/bin/env python@d}' $i >$i.new && \
    touch -r $i $i.new && \
    mv $i.new $i
done
popd


%build
for i in $(find . -name "setup.py" -not -path "./tests/*" -not -path "./docs/*"); do
    pushd ${i%/*}
    %py3_build
    popd
done

# Build documentation
%make_build -C docs/ html
rm docs/_build/html/.??*


%install
for i in $(find . -name "setup.py" -not -path "./tests/*" -not -path "./docs/*"); do
    pushd ${i%/*}
    %py3_install
    popd
done


%check
export PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitelib}/:tests/util/src/
for i in $(find . -name "setup.py" -not -path "./tests/*" -not -path "./docs/*"); do
    d=${i%/*}
    pytest-%{python3_version} ${i%/*} \
        --deselect=opentelemetry-sdk/tests/trace/test_trace.py::TestTracer::test_shutdown
done


%files -n python3-%{srcname}-api
%doc opentelemetry-api/{CHANGELOG.md,README.rst}
%license opentelemetry-api/LICENSE
%{python3_sitelib}/%{srcname}/
%exclude %{python3_sitelib}/%{srcname}/auto_instrumentation/
%exclude %{python3_sitelib}/%{srcname}/sdk/
%exclude %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}_api-*.egg-info/


%files -n python3-%{srcname}-auto-instrumentation
%doc opentelemetry-auto-instrumentation/{CHANGELOG.md,README.rst}
%license LICENSE
%{_bindir}/%{srcname}-auto-instrumentation
%{_bindir}/%{srcname}-bootstrap
%{python3_sitelib}/%{srcname}/auto_instrumentation/
%{python3_sitelib}/%{srcname}_auto_instrumentation-*.egg-info/


%files -n python3-%{srcname}-sdk
%doc opentelemetry-sdk/{CHANGELOG.md,README.rst}
%license opentelemetry-sdk/LICENSE
%{python3_sitelib}/%{srcname}/sdk/
%{python3_sitelib}/%{srcname}_sdk-*.egg-info/


%files -n python3-%{srcname}-ext-aiohttp-client
%doc ext/opentelemetry-ext-aiohttp-client/{CHANGELOG.md,README.rst}
%license ext/opentelemetry-ext-aiohttp-client/LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/aiohttp_client/
%{python3_sitelib}/%{srcname}_ext_aiohttp_client-*.egg-info/


%files -n python3-%{srcname}-ext-asgi
%doc ext/opentelemetry-ext-asgi/{CHANGELOG.md,README.rst}
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/asgi/
%{python3_sitelib}/%{srcname}_ext_asgi-*.egg-info/


# %%files -n python3-%%{srcname}-ext-datadog
# %%doc ext/opentelemetry-ext-datadog/{CHANGELOG.md,README.rst}
# %%dir %%{python3_sitelib}/%%{srcname}/ext/
# %%{python3_sitelib}/%%{srcname}/ext/datadog/
# %%{python3_sitelib}/%%{srcname}_ext_datadog-*.egg-info/


%files -n python3-%{srcname}-ext-dbapi
%doc ext/opentelemetry-ext-dbapi/{CHANGELOG.md,README.rst}
%license ext/opentelemetry-ext-dbapi/LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/dbapi/
%{python3_sitelib}/%{srcname}_ext_dbapi-*.egg-info/


%files -n python3-%{srcname}-ext-django
%doc ext/opentelemetry-ext-django/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/django/
%{python3_sitelib}/%{srcname}_ext_django-*.egg-info/


%files -n python3-%{srcname}-ext-flask
%doc ext/opentelemetry-ext-flask/{CHANGELOG.md,README.rst}
%license ext/opentelemetry-ext-flask/LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/flask/
%{python3_sitelib}/%{srcname}_ext_flask-*.egg-info/


%files -n python3-%{srcname}-ext-grpc
%doc ext/opentelemetry-ext-grpc/{CHANGELOG.md,README.rst}
%license ext/opentelemetry-ext-grpc/LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/grpc/
%{python3_sitelib}/%{srcname}_ext_grpc-*.egg-info/


%files -n python3-%{srcname}-ext-jaeger
%doc ext/opentelemetry-ext-jaeger/{CHANGELOG.md,README.rst}
%license ext/opentelemetry-ext-jaeger/LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/jaeger/
%{python3_sitelib}/%{srcname}_ext_jaeger-*.egg-info/


%files -n python3-%{srcname}-ext-jinja2
%doc ext/opentelemetry-ext-jinja2/{CHANGELOG.md,README.rst}
%license ext/opentelemetry-ext-jinja2/LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/jinja2/
%{python3_sitelib}/%{srcname}_ext_jinja2-*.egg-info/


%files -n python3-%{srcname}-ext-mysql
%doc ext/opentelemetry-ext-mysql/{CHANGELOG.md,README.rst}
%license ext/opentelemetry-ext-mysql/LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/mysql/
%{python3_sitelib}/%{srcname}_ext_mysql-*.egg-info/


# %%files -n python3-%%{srcname}-ext-opentracing-shim
# %%doc ext/opentelemetry-ext-opentracing-shim/{CHANGELOG.md,README.rst}
# %%license ext/opentelemetry-ext-opentracing-shim/LICENSE
# %%dir %%{python3_sitelib}/%%{srcname}/ext/
# %%{python3_sitelib}/%%{srcname}/ext/opentracing_shim/
# %%{python3_sitelib}/%%{srcname}_opentracing_shim-*.egg-info/


%files -n python3-%{srcname}-ext-opencensusexporter
%doc ext/opentelemetry-ext-opencensusexporter/{CHANGELOG.md,README.rst}
%license ext/opentelemetry-ext-opencensusexporter/LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/opencensusexporter/
%{python3_sitelib}/%{srcname}_ext_opencensusexporter-*.egg-info/


%files -n python3-%{srcname}-ext-prometheus
%doc ext/opentelemetry-ext-prometheus/{CHANGELOG.md,README.rst}
%license ext/opentelemetry-ext-prometheus/LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/prometheus/
%{python3_sitelib}/%{srcname}_ext_prometheus-*.egg-info/


%files -n python3-%{srcname}-ext-psycopg2
%doc ext/opentelemetry-ext-psycopg2/{CHANGELOG.md,README.rst}
%license ext/opentelemetry-ext-psycopg2/LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/psycopg2/
%{python3_sitelib}/%{srcname}_ext_psycopg2-*.egg-info/


%files -n python3-%{srcname}-ext-pymongo
%doc ext/opentelemetry-ext-pymongo/{CHANGELOG.md,README.rst}
%license ext/opentelemetry-ext-pymongo/LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/pymongo/
%{python3_sitelib}/%{srcname}_ext_pymongo-*.egg-info/


%files -n python3-%{srcname}-ext-pymysql
%doc ext/opentelemetry-ext-pymysql/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/pymysql/
%{python3_sitelib}/%{srcname}_ext_pymysql-*.egg-info/


%files -n python3-%{srcname}-ext-redis
%doc ext/opentelemetry-ext-redis/{CHANGELOG.md,README.rst}
%license LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/redis/
%{python3_sitelib}/%{srcname}_ext_redis-*.egg-info/


%files -n python3-%{srcname}-ext-requests
%doc ext/opentelemetry-ext-requests/{CHANGELOG.md,README.rst}
%license ext/opentelemetry-ext-requests/LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/requests/
%{python3_sitelib}/%{srcname}_ext_requests-*.egg-info/


%files -n python3-%{srcname}-ext-sqlalchemy
%doc ext/opentelemetry-ext-sqlalchemy/{CHANGELOG.md,README.rst}
%license ext/opentelemetry-ext-sqlalchemy/LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/sqlalchemy/
%{python3_sitelib}/%{srcname}_ext_sqlalchemy-*.egg-info/


%files -n python3-%{srcname}-ext-sqlite3
%doc ext/opentelemetry-ext-sqlite3/{CHANGELOG.md,README.rst}
%license ext/opentelemetry-ext-sqlite3/LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/sqlite3/
%{python3_sitelib}/%{srcname}_ext_sqlite3-*.egg-info/


%files -n python3-%{srcname}-ext-wsgi
%doc ext/opentelemetry-ext-wsgi/{CHANGELOG.md,README.rst}
%license ext/opentelemetry-ext-wsgi/LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/wsgi/
%{python3_sitelib}/%{srcname}_ext_wsgi-*.egg-info/


%files -n python3-%{srcname}-ext-zipkin
%doc ext/opentelemetry-ext-zipkin/{CHANGELOG.md,README.rst}
%license ext/opentelemetry-ext-zipkin/LICENSE
%dir %{python3_sitelib}/%{srcname}/ext/
%{python3_sitelib}/%{srcname}/ext/zipkin/
%{python3_sitelib}/%{srcname}_ext_zipkin-*.egg-info/


%files doc
%doc docs/_build/html/
%license LICENSE


%changelog
* Sat Feb 13 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.8.0-5
- Fix documentation build with new RTD theme (RHBZ #1919861)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.8.0-2
- Update requirements patch to drop version condition on PyMySQL (RHBZ #1858698)

* Thu Jun 18 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Sun May 24 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.7.1-1
- Initial RPM release
