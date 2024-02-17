%define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define libname %mklibname KPim6PimCommon
%define devname %mklibname KPim6PimCommon -d

Name: plasma6-pimcommon
Version:	24.01.96
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/pimcommon/-/archive/%{gitbranch}/pimcommon-%{gitbranchd}.tar.bz2#/pimcommon-20240217.tar.bz2
%else
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/pimcommon-%{version}.tar.xz
%endif
Summary: KDE library for personal information management
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6UiTools)
BuildRequires: cmake(Qt6UiPlugin)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6TextTemplate)
BuildRequires: cmake(KF6TextAutoCorrectionCore)
BuildRequires: cmake(KF6TextAutoCorrectionWidgets)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6TextAddonsWidgets)
BuildRequires: cmake(KF6TextCustomEditor)
BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KPim6AkonadiMime)
BuildRequires: cmake(KPim6IMAP)
BuildRequires: cmake(KPim6Libkdepim)
BuildRequires: cmake(KPim6AkonadiContactCore)
BuildRequires: cmake(KPim6AkonadiContactWidgets)
BuildRequires: cmake(KPim6AkonadiSearch)
BuildRequires: cmake(KPim6LdapCore)
BuildRequires: cmake(KPim6LdapWidgets)
BuildRequires: xsltproc
BuildRequires: sasl-devel
BuildRequires: boost-devel
BuildRequires: cmake ninja
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant

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
%autosetup -p1 -n pimcommon-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang libpimcommon6

%files -f libpimcommon6.lang
%{_datadir}/qlogging-categories6/pimcommon.categories
%{_datadir}/qlogging-categories6/pimcommon.renamecategories

%files -n %{libname}
%{_libdir}/*.so*
%{_libdir}/qt6/plugins/designer/pimcommon6widgets.so
%{_libdir}/qt6/plugins/designer/pimcommon6akonadiwidgets.so

%files -n %{devname}
%{_includedir}/*
%{_libdir}/cmake/*
