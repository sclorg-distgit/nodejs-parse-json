%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

# ava is not in fedora yet
%global enable_tests 0
%global module_name parse-json
%global gittag0 v2.2.0

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        2.2.0
Release:        4%{?dist}
Summary:        Parse JSON with more helpful errors

# vendor/parse.js is under WTFPL and rest code under MIT
License:        MIT and WTFPL
URL:            https://github.com/sindresorhus/parse-json
Source0:        https://github.com/sindresorhus/%{module_name}/archive/%{gittag0}.tar.gz#/%{module_name}-%{gittag0}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs010-runtime

%if 0%{?enable_tests}
%endif

%description
%{summary}.

%prep
%setup -q -n %{module_name}-%{version}
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json index.js vendor %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
node test.js
%endif

%files
%{!?_licensedir:%global license %doc}
%doc readme.md
%license license
%{nodejs_sitelib}/%{module_name}

%changelog
* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 2.2.0-4
- Use macro to find provides and requires

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 2.2.0-3
- Enable scl macros, fix license macro for el6

* Thu Oct 29 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.2.0-2
- Fix license tag

* Fri Sep 11 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.2.0-1
- Initial packaging