# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/newspaper
# catalog-date 2008-08-22 17:15:44 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-newspaper
Version:	1.0
Release:	3
Summary:	Typeset newsletters to resemble newspapers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/newspaper
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newspaper.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newspaper.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newspaper.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 754338
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719113
- texlive-newspaper
- texlive-newspaper
- texlive-newspaper
- texlive-newspaper

