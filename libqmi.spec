%define	oname	qmi
%define	major	0
%define	libname	%mklibname %{oname}-glib %{major}
%define	devname	%mklibname %{oname}-glib -d

Summary:	Library to control QMI devices
Name:		libqmi
Version:	1.4.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://cgit.freedesktop.org/libqmi/
Source0:	http://cgit.freedesktop.org/libqmi/snapshot/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.32
BuildRequires:	pkgconfig(gobject-2.0)

%description
A GLib/GIO based library to control QMI devices

%package -n %{oname}-tools
Summary:	Helper utilities to control QMI devices
Group:		System/Configuration/Networking

%description -n %{oname}-tools
This package contains command line tools to manage such devices.

%package -n %{libname}
Summary:	Library to control QMI devices
Group:		System/Libraries

%description -n %{libname}
A GLib/GIO based library to control QMI devices

%package -n %{devname}
Summary:	Library to control QMI devices - Development files
Group:		Development/C
Requires:	%{libname} = %{version}

%description -n %{devname}
This package contains files required to link sources against libqmi.

%prep
%setup -q

%build
./autogen.sh
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{oname}-tools
%{_bindir}/qmi-network
%{_bindir}/qmicli

%files -n %{libname}
%{_libdir}/libqmi-glib.so.%{major}*

%files -n %{devname}
%{_includedir}/libqmi-glib/
%{_libdir}/libqmi-glib.so
%{_libdir}/pkgconfig/qmi-glib.pc

