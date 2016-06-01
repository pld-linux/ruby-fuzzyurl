#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	fuzzyurl
Summary:	A library for non-strict parsing, construction, and wildcard-matching of URLs
Name:		ruby-%{pkgname}
Version:	0.8.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	28edf07678a73ce1252a9a394b5fe502
URL:		https://github.com/gamache/fuzzyurl.rb
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-minitest >= 4.7.0
BuildRequires:	ruby-mocha >= 0.13.3
BuildRequires:	ruby-pry
BuildRequires:	ruby-rake >= 10.0.4
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for non-strict parsing, construction, and wildcard-matching
of URLs.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
