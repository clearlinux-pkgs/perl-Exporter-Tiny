#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Exporter-Tiny
Version  : 1.004003
Release  : 46
URL      : https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Exporter-Tiny-1.004003.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Exporter-Tiny-1.004003.tar.gz
Summary  : 'an exporter with the features of Sub::Exporter but only core dependencies'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Exporter-Tiny-license = %{version}-%{release}
Requires: perl-Exporter-Tiny-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::More)
BuildRequires : perl(Test::Warnings)

%description
NAME
Exporter::Tiny - an exporter with the features of Sub::Exporter but only
core dependencies

%package dev
Summary: dev components for the perl-Exporter-Tiny package.
Group: Development
Provides: perl-Exporter-Tiny-devel = %{version}-%{release}
Requires: perl-Exporter-Tiny = %{version}-%{release}

%description dev
dev components for the perl-Exporter-Tiny package.


%package license
Summary: license components for the perl-Exporter-Tiny package.
Group: Default

%description license
license components for the perl-Exporter-Tiny package.


%package perl
Summary: perl components for the perl-Exporter-Tiny package.
Group: Default
Requires: perl-Exporter-Tiny = %{version}-%{release}

%description perl
perl components for the perl-Exporter-Tiny package.


%prep
%setup -q -n Exporter-Tiny-1.004003
cd %{_builddir}/Exporter-Tiny-1.004003

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Exporter-Tiny
cp %{_builddir}/Exporter-Tiny-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Exporter-Tiny/b288b1bcff3334631a50e17207149b915027c134 || :
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
/usr/share/man/man3/Exporter::Shiny.3
/usr/share/man/man3/Exporter::Tiny.3
/usr/share/man/man3/Exporter::Tiny::Manual::Etc.3
/usr/share/man/man3/Exporter::Tiny::Manual::Exporting.3
/usr/share/man/man3/Exporter::Tiny::Manual::Importing.3
/usr/share/man/man3/Exporter::Tiny::Manual::QuickStart.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Exporter-Tiny/b288b1bcff3334631a50e17207149b915027c134

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
