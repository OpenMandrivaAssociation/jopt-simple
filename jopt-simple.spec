Name:		jopt-simple
Version:	5.0.4
Release:	1
Summary:	Command line option parser for Java
Group:		Development/Java
License:	MIT
URL:		https://jopt-simple.github.io/jopt-simple/
Source0:	https://github.com/jopt-simple/jopt-simple/archive/refs/tags/jopt-simple-%{version}.tar.gz#/jopt-simple-%{version}.tar.gz

BuildArch:	noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildRequires:	mvn(org.sonatype.oss:oss-parent:pom::)
BuildSystem:	maven
# antrun is only used to publish the site. It is not in the toolchain.
%global sysjar_drops --drop org.apache.maven.plugins:maven-antrun-plugin
BuildOption(install):	--file-name jopt-simple

%description
JOpt Simple parses command-line options. Gradle pins 5.0.4 for the
profiler API. The 6.0 line is still an alpha.

%prep
%autosetup -n jopt-simple-jopt-simple-%{version}

%files -f .mfiles
%doc LICENSE.txt README.md
