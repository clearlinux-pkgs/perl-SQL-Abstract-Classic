#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-SQL-Abstract-Classic
Version  : 1.91
Release  : 17
URL      : https://cpan.metacpan.org/authors/id/R/RI/RIBASUSHI/SQL-Abstract-Classic-1.91.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RI/RIBASUSHI/SQL-Abstract-Classic-1.91.tar.gz
Summary  : 'Generate SQL from Perl data structures'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-SQL-Abstract-Classic-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Moo)
BuildRequires : perl(SQL::Abstract)
BuildRequires : perl(SQL::Abstract::Test)
BuildRequires : perl(Sub::Quote)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::Exception)
BuildRequires : perl(Test::Warn)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the perl-SQL-Abstract-Classic package.
Group: Development
Provides: perl-SQL-Abstract-Classic-devel = %{version}-%{release}
Requires: perl-SQL-Abstract-Classic = %{version}-%{release}

%description dev
dev components for the perl-SQL-Abstract-Classic package.


%package perl
Summary: perl components for the perl-SQL-Abstract-Classic package.
Group: Default
Requires: perl-SQL-Abstract-Classic = %{version}-%{release}

%description perl
perl components for the perl-SQL-Abstract-Classic package.


%prep
%setup -q -n SQL-Abstract-Classic-1.91
cd %{_builddir}/SQL-Abstract-Classic-1.91

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/SQL::Abstract::Classic.3
/usr/share/man/man3/SQL::Abstract::Util.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
