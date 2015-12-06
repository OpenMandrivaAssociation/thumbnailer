%define snapshot_date 20150113

%define major 0
%define libname %mklibname thumbnailer %{major}
%define develname %mklibname thumbnailer -d

Name:		thumbnailer
Version:	1.1
Release:	0.%{snapshot_date}.1
Summary:	Thumbnail generator for all kinds of files

Group:		Graphics
License:	LGPLv3
URL:		https://launchpad.net/thumbnailer
# bzr branch lp:thumbnailer
# tar cjf thumbnailer-%{snapshot_date}.tar.bz2 thumbnailer
Source:		thumbnailer-%{snapshot_date}.tar.bz2
Patch0:		thumbnailer-disable-gtest.patch
BuildRequires:	cmake
BuildRequires:	qt5-macros
BuildRequires:	qmake5
BuildRequires:	gtest-devel
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)

%description
A simple shared library that produces and stores thumbnails of image,
audio and video files according to the Freedesktop thumbnail specification.

%package 	-n %{libname}
Summary:	A simple shared library that produces and stores thumbnails
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{_lib}thumbnailer1.1.0 < %{version}-%{release}

%description	-n %{libname}
A simple shared library that produces and stores thumbnails.

%package	-n %{develname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}

%description	-n %{develname}
Development files for %{name}.


%prep
%setup -qn %{name}
%patch0 -p1
%cmake_qt5

%build
%make

%install
%makeinstall_std -C build
mv %{buildroot}/usr/etc %{buildroot}

%files
%doc COPYING
%{_sysconfdir}/apport/blacklist.d/%{name}
%{_libdir}/%{name}
%{_datadir}/dbus-1/services/com.canonical.Thumbnailer.service
%{_datadir}/glib-2.0/schemas/com.canonical.Unity.Thumbnailer.gschema.xml
%{_datadir}/%{name}
%{_libdir}/qt5/qml/Ubuntu/Thumbnailer.0.1

%files -n %{libname}
%doc COPYING
%{_libdir}/*.so.*%{major}*

%files -n %{develname}
%doc COPYING
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

