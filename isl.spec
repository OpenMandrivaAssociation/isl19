%define major 10

%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define staticname %mklibname %{name} -d -s

Summary:	Integer Set Library
Name:		isl
Version:	0.11.1
Release:	1
License:	MIT
Group:		System/Libraries
URL:		http://www.kotnet.org/~skimo/isl/
Source0:	http://www.kotnet.org/~skimo/isl/isl-%version.tar.lzma
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

%package -n	%{libname}
Summary:	Integer Set Library
Group:		System/Libraries

%description -n	%{libname}
isl is a library for manipulating sets and relations of integer points
bounded by linear constraints. Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, computing the lexicographic
minimum using parametric integer programming, coalescing and parametric
vertex enumeration.

It also includes an ILP solver based on generalized basis reduction,
transitive closures on maps (which may encode infinite graphs),
dependence analysis and bounds on piecewise step-polynomials.

%package -n	%{develname}
Summary:	Development files for the isl Integer Set Library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
Header files for the isl Integer Set Library.

isl is a library for manipulating sets and relations of integer points
bounded by linear constraints. Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, computing the lexicographic
minimum using parametric integer programming, coalescing and parametric
vertex enumeration.

It also includes an ILP solver based on generalized basis reduction,
transitive closures on maps (which may encode infinite graphs),
dependence analysis and bounds on piecewise step-polynomials.

%package -n	%{staticname}
Summary:	Static library files for the isl Integer Set Library
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{staticname}
Static library files for the isl Integer Set Library.

isl is a library for manipulating sets and relations of integer points
bounded by linear constraints. Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, computing the lexicographic
minimum using parametric integer programming, coalescing and parametric
vertex enumeration.

It also includes an ILP solver based on generalized basis reduction,
transitive closures on maps (which may encode infinite graphs),
dependence analysis and bounds on piecewise step-polynomials.

%prep
%setup -q
autoreconf -fi

%build
%configure
%make

%check
# All tests must pass
make check

%install
%makeinstall_std

%files -n %libname
%_libdir/libisl.so.%{major}*

%files -n %develname
%_libdir/libisl.so
%_includedir/*
%_libdir/pkgconfig/*.pc

%files -n %staticname
%_libdir/*.a
