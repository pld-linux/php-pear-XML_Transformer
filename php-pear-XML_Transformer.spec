%include	/usr/lib/rpm/macros.php
%define         _class          XML
%define         _subclass       Transformer
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - XML Transformations in PHP
Summary(pl):	%{_pearname} - Transformacje XML w PHP
Name:		php-pear-%{_pearname}
Version:	0.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With the XML_Transformer class one can easily bind PHP functionality
to XML tags, thus transforming the input XML tree into an output XML
tree without the need for XSLT. Single XML elements can be overloaded
with PHP functions, methods and static method calls, XML namespaces
can be registered to be handled by PHP classes.

%description -l pl
Z klas± XML_Transformer mo¿na ³atwo zwi±zaæ funkcjonalno¶æ PHP z
tagami XML, transformuj±c wej¶ciowe drzewo XML w wyj¶ciowe drzewo XML
bez potrzeby stosowania XSLT. Pojedyñczy element XML mo¿e byæ
przeci±¿ony funkcjami PHP, metodami i statycznymi wywo³aniami metod,
przestrzeñ nazw XML mo¿e byæ zarejestrowana, aby mo¿na by³o je
obs³ugiwaæ przez klasy PHP.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
