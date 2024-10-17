%define upstream_name    Math-Gradient
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Calculate Gradients Between Multiple Numbers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tgz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Math::Gradient is used to calculate smooth transitions between numerical
values (also known as a "Gradient"). I wrote this module mainly to mix
colours, but it probably has several other applications. Methods are
supported to handle both basic and multiple-point gradients, both with
scalars and arrays.

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
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 655043
- rebuild for updated spec-helper

* Sun Aug 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 419891
- import perl-Math-Gradient


* Sun Aug 23 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist
