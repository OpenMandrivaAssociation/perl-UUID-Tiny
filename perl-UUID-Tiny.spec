%define upstream_name    UUID-Tiny
%define upstream_version 1.04
Name:		perl-%{upstream_name}
Version:	1.04
Release:	1

Summary:	Pure Perl UUID functions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/UUID-Tiny
Source0:	https://cpan.metacpan.org/authors/id/C/CA/CAUGUSTIN/UUID-Tiny-1.04.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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

