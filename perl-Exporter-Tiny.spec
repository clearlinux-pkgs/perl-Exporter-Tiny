#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Exporter-Tiny
Version  : 0.044
Release  : 13
URL      : http://search.cpan.org/CPAN/authors/id/T/TO/TOBYINK/Exporter-Tiny-0.044.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/T/TO/TOBYINK/Exporter-Tiny-0.044.tar.gz
Summary  : 'an exporter with the features of Sub::Exporter but only core dependencies'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Exporter-Tiny-doc
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::More)
BuildRequires : perl(Test::Warnings)

%description
NAME
Exporter::Tiny - an exporter with the features of Sub::Exporter but only
core dependencies

%package doc
Summary: doc components for the perl-Exporter-Tiny package.
Group: Documentation

%description doc
doc components for the perl-Exporter-Tiny package.


%prep
%setup -q -n Exporter-Tiny-0.044

%build
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.24.0/Exporter/Shiny.pm
/usr/lib/perl5/site_perl/5.24.0/Exporter/Tiny.pm
/usr/lib/perl5/site_perl/5.24.0/Exporter/Tiny/Manual/Etc.pod
/usr/lib/perl5/site_perl/5.24.0/Exporter/Tiny/Manual/Exporting.pod
/usr/lib/perl5/site_perl/5.24.0/Exporter/Tiny/Manual/Importing.pod
/usr/lib/perl5/site_perl/5.24.0/Exporter/Tiny/Manual/QuickStart.pod

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
