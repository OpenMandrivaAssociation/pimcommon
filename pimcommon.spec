%define major 5
%define libname %mklibname KF5PimCommon %{major}
%define devname %mklibname KF5PimCommon -d

Name: pimcommon
Version:	23.08.5
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
# Drop support for KTextAddons 1.2. We ship >= 1.3
# and supporting both causes the cmake dependency generator
# to require 2 conflicting versions
Patch0: pimcommon-23.04.1-drop-ktextaddons-1.2.patch
Summary: KDE library for personal information management
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5UiTools)
BuildRequires: cmake(KPim5Akonadi)
BuildRequires: cmake(KPim5AkonadiMime)
BuildRequires: cmake(KF5Libkdepim)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5CalendarCore)
BuildRequires: cmake(KPim5IMAP)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5PimTextEdit)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5Purpose)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KPim5AkonadiContact)
BuildRequires: cmake(KPim5AkonadiSearch)
BuildRequires: cmake(KPim5Ldap)
BuildRequires: cmake(Grantlee5)
BuildRequires: cmake(KF5TextAutoCorrectionCore)
BuildRequires: cmake(KF5TextAutoCorrectionWidgets)
BuildRequires: xsltproc
BuildRequires: sasl-devel
BuildRequires: boost-devel
BuildRequires: cmake ninja
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
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
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang libpimcommon

%files -f libpimcommon.lang
%{_datadir}/qlogging-categories5/pimcommon.categories
%{_datadir}/qlogging-categories5/pimcommon.renamecategories

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/qt5/plugins/designer/pimcommon5widgets.so
%{_libdir}/qt5/plugins/designer/pimcommon5akonadiwidgets.so

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
%doc %{_docdir}/qt5/*.{tags,qch}
