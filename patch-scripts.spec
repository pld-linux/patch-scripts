%include	/usr/lib/rpm/macros.perl
Summary:	Collection of scripts for managing patches
Summary(pl.UTF-8):	Zestaw skryptów do zarządzania łatami
Name:		patch-scripts
Version:	0.20
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.zip.com.au/~akpm/linux/patches/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a74650ccd565148b92dae8dd402afd3b
URL:		http://www.zip.com.au/~akpm/linux/patches
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of scripts for managing patches (used for example for
kernel patches management).

%description -l pl.UTF-8
Zestaw skryptów do zarządzania łatami (używany na przykład przy
zarządzaniu łatami na jądro).

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

for f in *; do
	[ -x "$f" -a ! -d "$f" ] && install "$f" $RPM_BUILD_ROOT%{_datadir}/%{name}/
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/*
