%include	/usr/lib/rpm/macros.php
%define         _class          XML
%define         _subclass       Transformer
%define		_pearname	%{_class}_%{_subclass}
%define		_status		stable

Summary:	%{_pearname} - XML Transformations in PHP
Summary(pl):	%{_pearname} - Transformacje XML w PHP
Name:		php-pear-%{_pearname}
Version:	0.9.0
Release:	1
License:	PHP 3.00
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	356aeec6da49c5d690d17564bb8c5792
URL:		http://pear.php.net/package/XML_Transformer/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With the XML_Transformer class one can easily bind PHP functionality
to XML tags, thus transforming the input XML tree into an output XML
tree without the need for XSLT. Single XML elements can be overloaded
with PHP functions, methods and static method calls, XML namespaces
can be registered to be handled by PHP classes.

This class has in PEAR status: %{_status}.

%description -l pl
Z klas± XML_Transformer mo¿na ³atwo zwi±zaæ funkcjonalno¶æ PHP z
tagami XML, transformuj±c wej¶ciowe drzewo XML w wyj¶ciowe drzewo XML
bez potrzeby stosowania XSLT. Pojedyñczy element XML mo¿e byæ
przeci±¿ony funkcjami PHP, metodami i statycznymi wywo³aniami metod,
przestrzeñ nazw XML mo¿e byæ zarejestrowana, aby mo¿na by³o je
obs³ugiwaæ przez klasy PHP.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/{Driver,Namespace}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Driver/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Driver
install %{_pearname}-%{version}/%{_subclass}/Namespace/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Namespace

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Driver
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Namespace
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Driver/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Namespace/*.php
