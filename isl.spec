%define major 15
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define staticname %mklibname %{name} -s -d
# (tpg) disable it untill gdb will be fixed
%define _python_bytecompile_build 0

# (tpg) optimize it a bit
%global optflags %optflags -O3

Summary:	Integer Set Library
Name:		isl
Version:	0.20
Release:	1
License:	MIT
Group:		System/Libraries
Url:		git://repo.or.cz/isl.git
Source0:	http://isl.gforge.inria.fr/isl-%{version}.tar.xz
BuildRequires:	gmp-devel

%description
isl is a library for manipulating sets and relations of integer points
bounded by linear constraints. Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, computing the lexicographic
minimum using parametric integer programming, coalescing and parametric
vertex enumeration.

It also includes an ILP solver based on generalized basis reduction,
transitive closures on maps (which may encode infinite graphs),
dependence analysis and bounds on piecewise step-polynomials.

%package -n %{libname}
Summary:	Integer Set Library
Group:		System/Libraries

%description -n %{libname}
isl is a library for manipulating sets and relations of integer points
bounded by linear constraints. Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, computing the lexicographic
minimum using parametric integer programming, coalescing and parametric
vertex enumeration.

It also includes an ILP solver based on generalized basis reduction,
transitive closures on maps (which may encode infinite graphs),
dependence analysis and bounds on piecewise step-polynomials.

%package -n %{devname}
Summary:	Development files for the isl Integer Set Library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Header files for the isl Integer Set Library.

%package -n %{staticname}
Summary:	Static library for the isl Integer Set Library
Group:		Development/C
Requires:	%{devname} = %{EVRD}

%description -n %{staticname}
Static library for the isl Integer Set Library

%prep
%autosetup -p1
autoreconf -fi

%build
%configure --enable-static
%make_build

%check
# All tests must pass
make check

%install
%make_install

mkdir -p %{buildroot}/%{_datadir}/gdb/auto-load/%{_libdir}
mv %{buildroot}/%{_libdir}/*.py %{buildroot}/%{_datadir}/gdb/auto-load/%{_libdir}

%files -n %{libname}
%{_libdir}/libisl.so.%{major}
%{_libdir}/libisl.so.%{major}.[0-9].[0-9]

%files -n %{devname}
%{_libdir}/libisl.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gdb/auto-load/%{_libdir}/*%{name}*-gdb.py

%files -n %{staticname}
%{_libdir}/*.a
