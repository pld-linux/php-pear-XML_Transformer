%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Transformer
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - XML transformations in PHP
Summary(pl):	%{_pearname} - transformacje XML-a w PHP
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	11dc89fdad2195a939354b71a568bacf
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

In PEAR status of this package is: %{_status}.

%description -l pl
Z klas� XML_Transformer mo�na �atwo zwi�za� funkcjonalno�� PHP z
tagami XML, transformuj�c wej�ciowe drzewo XML w wyj�ciowe drzewo XML
bez potrzeby stosowania XSLT. Pojedynczy element XML mo�e by�
przeci��ony funkcjami PHP, metodami i statycznymi wywo�aniami metod,
przestrze� nazw XML mo�e by� zarejestrowana, aby mo�na by�o je
obs�ugiwa� przez klasy PHP.

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
%doc %{_pearname}-%{version}/{README,%{_subclass}/Tests}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
