%define major 5
%define libname %mklibname KF5PimCommon %{major}
%define devname %mklibname KF5PimCommon -d

Name: pimcommon
Version:	19.11.80
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for personal information management
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5UiTools)
BuildRequires: cmake(KF5Akonadi)
BuildRequires: cmake(KF5AkonadiMime)
BuildRequires: cmake(KF5Libkdepim)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KF5IMAP)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5PimTextEdit)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5Purpose)
BuildRequires: cmake(Grantlee5)
BuildRequires: xsltproc
BuildRequires: sasl-devel
BuildRequires: boost-devel
Obsoletes:	kdepim-core < 3:17.04.0
Obsoletes:	kdepim-core = 3:17.04.0
Obsoletes:	storageservicemanager < 3:17.04.0
Provides:	storageservicemanager = 3:17.04.0

%description
KDE library for personal information management.

%package -n %{libname}
Summary: KDE library for personal information management
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for personal information management.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%apply_patches
%cmake_kde5 -G "Unix Makefiles"

%build
%make -C build

%install
%makeinstall_std -C build
%find_lang libpimcommon

%files -f libpimcommon.lang
%{_datadir}/qlogging-categories5/pimcommon.categories
%{_datadir}/qlogging-categories5/pimcommon.renamecategories

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/qt5/plugins/designer/pimcommonwidgets.so

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
