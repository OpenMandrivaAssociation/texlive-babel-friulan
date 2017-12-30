Name:		texlive-babel-friulan
Version:	1.3
Release:	1
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
%{_texmfdistdir}/tex/generic/babel-friulan
%doc %{_texmfdistdir}/doc/generic/babel-friulan
#- source
%doc %{_texmfdistdir}/source/generic/babel-friulan

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
