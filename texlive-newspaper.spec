Name:		texlive-newspaper
Version:	15878
Release:	1
Summary:	Typeset newsletters to resemble newspapers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/newspaper
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newspaper.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newspaper.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newspaper.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The newspaper package redefines the page style and \maketitle
command to produce a typeset page similar to that off a
newspaper. It also provides several commands that (when used
with other packages) simplify the writing of articles in a
newspaper-style column format.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/newspaper/newspaper.sty
%doc %{_texmfdistdir}/doc/latex/newspaper/Figure1.pdf
%doc %{_texmfdistdir}/doc/latex/newspaper/Figure2.pdf
%doc %{_texmfdistdir}/doc/latex/newspaper/README
%doc %{_texmfdistdir}/doc/latex/newspaper/atom.jpg
%doc %{_texmfdistdir}/doc/latex/newspaper/newspaper.pdf
%doc %{_texmfdistdir}/doc/latex/newspaper/newspaperExample.tex
#- source
%doc %{_texmfdistdir}/source/latex/newspaper/newspaper.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
