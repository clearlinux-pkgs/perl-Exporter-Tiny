#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Exporter-Tiny
Version  : 1.002001
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Exporter-Tiny-1.002001.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Exporter-Tiny-1.002001.tar.gz
Summary  : 'an exporter with the features of Sub::Exporter but only core dependencies'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Exporter-Tiny-license = %{version}-%{release}
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

%description dev
dev components for the perl-Exporter-Tiny package.


%package license
Summary: license components for the perl-Exporter-Tiny package.
Group: Default

%description license
license components for the perl-Exporter-Tiny package.


%prep
%setup -q -n Exporter-Tiny-1.002001

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Exporter-Tiny
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Exporter-Tiny/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.1/Exporter/Shiny.pm
/usr/lib/perl5/vendor_perl/5.28.1/Exporter/Tiny.pm
/usr/lib/perl5/vendor_perl/5.28.1/Exporter/Tiny/Manual/Etc.pod
/usr/lib/perl5/vendor_perl/5.28.1/Exporter/Tiny/Manual/Exporting.pod
/usr/lib/perl5/vendor_perl/5.28.1/Exporter/Tiny/Manual/Importing.pod
/usr/lib/perl5/vendor_perl/5.28.1/Exporter/Tiny/Manual/QuickStart.pod

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
/usr/share/package-licenses/perl-Exporter-Tiny/LICENSE
