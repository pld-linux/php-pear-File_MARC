%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	MARC
%define		_status		beta
%define		_pearname	File_MARC
Summary:	%{_pearname} - Parse, modify, and create MARC records
Summary(pl.UTF-8):	%{_pearname} - parsowanie, modyfikacja oraz tworzenie rekordów MARC
Name:		php-pear-%{_pearname}
Version:	0.6.2
Release:	1
License:	GNU Lesser General Public License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	005947de815285ce96ff8ca82cb6c15a
URL:		http://pear.php.net/package/File_MARC/
BuildRequires:	php-pear-PEAR >= 1:1.4.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.4.0
Requires:	php-pear-Structures_LinkedList
Obsoletes:	php-pear-File_MARC-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The standard for machine-readable cataloging (MARC) records is
documented at http://loc.gov/marc/. This package enables you to read
existing MARC records from a file, string, or (using the YAZ
extension), from a Z39.50 source. You can also use this package to
create new MARC records.

This package is based on the PHP MARC package, originally called
"php-marc", that is part of the Emilda Project
(http://www.emilda.org). Christoffer Landtman generously agreed to
make the "php-marc" code available under the GNU LGPL so it could be
used as the basis of this PEAR package.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa ta obsługuję standard czytelnych dla komputerów rekordów
katalogowania (MARC) opisanych na stronie http://loc.gov/marc/ .
Pakiet ten umożliwia odczyt istniejących rekordów z pliku, łańcucha
znaków czy też (przy użyciu rozszerzenia YAZ) ze źródła Z39.50.
Możliwe jest także tworzenie nowych rekordów MARC.

Pakiet ten oparty jest na projekcie PHP MARC, początkowo nazwanym
"php-marc" będącym częścią projektu Emilda (http://www.emilda.org/).
Christoffer Landtman zgodził się na udostępnienie kodu "php-marc" na
zasadach licencji GNU LGPL aby mógł się on stać podstawą tej klasy
PEAR.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

mv docs/File_MARC/examples .
mv docs/%{_pearname}/{CHANGELOG,LICENSE} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/File/MARC.php
%{php_pear_dir}/File/MARCBASE.php
%{php_pear_dir}/File/MARCXML.php
%{php_pear_dir}/File/MARC

%{_examplesdir}/%{name}-%{version}
