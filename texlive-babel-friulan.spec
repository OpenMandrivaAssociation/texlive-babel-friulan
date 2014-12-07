# revision 30361
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/friulan
# catalog-date 2013-05-04 11:13:00 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-babel-friulan
Version:	20130504
Release:	8
Summary:	Babel/Polyglossia support for Friulan(Furlan)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/friulan
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-friulan.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-friulan.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-friulan.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a language description file that enables
support of Friulan either with babel or with polyglossia.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-friulan/friulan.ldf
%doc %{_texmfdistdir}/doc/generic/babel-friulan/friulan.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-friulan/friulan.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
