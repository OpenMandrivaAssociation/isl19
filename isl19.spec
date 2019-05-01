%define major 19
%define libname %mklibname isl %{major}

# (tpg) optimize it a bit
%global optflags %optflags -O3

Summary:	Old version of the Integer Set Library
Name:		isl19
Version:	0.20
Release:	4
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

This is an old version of the ISL library, provided for binary
compatibility with old code only.

%package -n %{libname}
Summary:	Old version of the Integer Set Library
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

This is an old version of the ISL library, provided for binary
compatibility with old code only.

%prep
%autosetup -p1 -n isl-%{version}
autoreconf -fi

%build
%configure --enable-static
%make_build

%check
# All tests must pass
make check

%install
%make_install

# No -devel for compat packages
rm -rf	%{buildroot}%{_libdir}/libisl.so \
	%{buildroot}%{_libdir}/*.{a,py} \
	%{buildroot}%{_libdir}/pkgconfig \
	%{buildroot}%{_includedir}

%files -n %{libname}
%{_libdir}/libisl.so.%{major}
%{_libdir}/libisl.so.%{major}.[0-9].[0-9]
