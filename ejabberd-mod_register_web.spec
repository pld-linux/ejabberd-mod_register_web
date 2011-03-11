%define		snap	r1111

Summary:	Web to register account
Summary(pl.UTF-8):	Natywne sterowniki do MySQL-a dla demona ejabberd
Name:		ejabberd-mod_xmlrpc
Version:	0
Release:	0.%{snap}.1
License:	GPL
Group:		Applications/Communications
# svn export https://svn.process-one.net/ejabberd-modules/mod_register_web/trunk mod_register_web
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	c591b03e2331fcfc12c4e13a7cf23c2d
URL:		 http://www.ejabberd.im/mod_register_web
BuildRequires:	erlang >= R9C
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a web page where users can register Jabber accounts,
change password and other related tasks.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ejabberd/ebin

install *.beam $RPM_BUILD_ROOT%{_libdir}/ejabberd/ebin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
