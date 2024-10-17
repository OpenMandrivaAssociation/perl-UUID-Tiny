%define upstream_name    UUID-Tiny
%define upstream_version 1.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Pure Perl UUID functions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/UUID/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Time::HiRes)
BuildArch:	noarch

%description
UUID::Tiny is a lightweight, low dependency Pure Perl module for UUID
creation and testing. This module provides the creation of version 1 time
based UUIDs (using random multicast MAC addresses), version 3 MD5 based
UUIDs, version 4 random UUIDs, and version 5 SHA-1 based UUIDs.

ATTENTION! UUID::Tiny uses Perl's 'rand()' to create the basic random
numbers, so the created v4 UUIDs are *not* cryptographically strong!

No fancy OO interface, no plethora of different UUID representation formats
and transformations - just string and binary. Conversion, test and time
functions equally accept UUIDs and UUID strings, so don't bother to convert
UUIDs for them!

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/UUID/

%changelog
* Thu Apr 29 2010 Michael Scherer <misc@mandriva.org> 1.30.0-1mdv2010.1
+ Revision: 541073
- import perl-UUID-Tiny


* Thu Apr 29 2010 cpan2dist 1.03-1mdv
- initial mdv release, generated with cpan2dist
