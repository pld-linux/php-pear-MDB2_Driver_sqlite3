%define		status		beta
%define		pearname	MDB2_Driver_sqlite3
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - sqlite MDB2 driver
Summary(pl.UTF-8):	%{pearname} - sterownik sqlite dla MDB2
Name:		php-pear-%{pearname}
Version:	0.1
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	MDB2_Driver_sqlite3.tar.bz2
# Source0-md5:	1db962da9d548c5506d6ec598b1e737e
#URL:		https://github.com/owncloud/core/tree/master/lib/MDB2/Driver
URL:		http://thread.gmane.org/gmane.comp.php.pear.devel/50535
BuildRequires:	php-pear-PEAR >= 1:1.9.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.3.0
Requires:	php(sqlite3)
Requires:	php-pear
Requires:	php-pear-MDB2 >= 1:2.5.0-0.b4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the SQLite3 MDB2 driver.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Sterownik SQLite3 dla MDB2.

Ta klasa ma w PEAR status: %{status}.

%prep
%setup -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/MDB2/Driver
cp -a %{pearname}/* $RPM_BUILD_ROOT%{php_pear_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc install.log
#%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/MDB2/Driver/Datatype/sqlite3.php
%{php_pear_dir}/MDB2/Driver/Manager/sqlite3.php
%{php_pear_dir}/MDB2/Driver/Native/sqlite3.php
%{php_pear_dir}/MDB2/Driver/Reverse/sqlite3.php
%{php_pear_dir}/MDB2/Driver/Function/sqlite3.php
%{php_pear_dir}/MDB2/Driver/sqlite3.php
