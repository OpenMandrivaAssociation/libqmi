%define oname qmi
%define major 5
%define libname %mklibname %{oname}-glib %{major}
%define devname %mklibname %{oname}-glib -d
%define debug_package %{nil}

Summary:	Library to control QMI devices
Name:		libqmi
Version:	1.24.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://cgit.freedesktop.org/libqmi/
Source0:	http://freedesktop.org/software/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.32
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gudev-1.0) >= 147
BuildRequires:	pkgconfig(mbim-glib)

%description
A GLib/GIO based library to control QMI devices.

%package -n %{oname}-tools
Summary:	Helper utilities to control QMI devices
Group:		System/Configuration/Networking

%description -n %{oname}-tools
This package contains command line tools to manage such devices.

%package -n %{libname}
Summary:	Library to control QMI devices
Group:		System/Libraries
Obsoletes:	%{mklibname qmi-glib 1} < 1.14.0

%description -n %{libname}
A GLib/GIO based library to control QMI devices.

%package -n %{devname}
Summary:	Library to control QMI devices - Development files
Group:		Development/C
Requires:	%{libname} = %{version}

%description -n %{devname}
This package contains files required to link sources against libqmi.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	--disable-gtk-doc-html \
	--enable-more-warnings=no

%make_build

%install
%make_install

# (tpg) kill docs
rm -rf %{buildroot}%{_datadir}/gtk-doc/

%files -n %{oname}-tools
%{_datadir}/bash-completion/completions/qmicli
%{_bindir}/qmi-network
%{_bindir}/qmi-firmware-update
%{_bindir}/qmicli
%{_libexecdir}/qmi-proxy
%{_mandir}/man1/qmi*.1.*

%files -n %{libname}
%{_libdir}/libqmi-glib.so.%{major}*

%files -n %{devname}
%{_includedir}/libqmi-glib/
%{_libdir}/libqmi-glib.so
%{_libdir}/pkgconfig/qmi-glib.pc
