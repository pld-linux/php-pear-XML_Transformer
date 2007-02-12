%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Transformer
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - XML transformations in PHP
Summary(pl.UTF-8):	%{_pearname} - transformacje XML-a w PHP
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	4
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	11dc89fdad2195a939354b71a568bacf
URL:		http://pear.php.net/package/XML_Transformer/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(pcre)
Requires:	php(xml)
Requires:	php-common < 3:5.1
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-XML_Util >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With the XML_Transformer class one can easily bind PHP functionality
to XML tags, thus transforming the input XML tree into an output XML
tree without the need for XSLT. Single XML elements can be overloaded
with PHP functions, methods and static method calls, XML namespaces
can be registered to be handled by PHP classes.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Z klasą XML_Transformer można łatwo związać funkcjonalność PHP z
tagami XML, transformując wejściowe drzewo XML w wyjściowe drzewo XML
bez potrzeby stosowania XSLT. Pojedynczy element XML może być
przeciążony funkcjami PHP, metodami i statycznymi wywołaniami metod,
przestrzeń nazw XML może być zarejestrowana, aby można było je
obsługiwać przez klasy PHP.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

install -d ./%{php_pear_dir}/tests
mv ./%{php_pear_dir}/{%{_class}/%{_subclass}/Tests,tests/%{_pearname}}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
