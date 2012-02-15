# Generated from sequel-3.31.0.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	sequel

Summary:	The Database Toolkit for Ruby
Name:		rubygem-%{rbname}

Version:	3.31.0
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://sequel.rubyforge.org
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
The Database Toolkit for Ruby

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%{_bindir}/sequel
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/plugins
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/model
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/database
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/adapters/
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/adapters/swift
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/adapters/jdbc
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/adapters/ado
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/adapters/do
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/adapters/odbc
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/adapters/utils
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/adapters/shared
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/extensions
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/dataset
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/connection_pool
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/sequel
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/doc
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/doc/release_notes
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb



%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/adapters/swift/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/adapters/jdbc/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/adapters/ado/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/adapters/do/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/adapters/odbc/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/adapters/utils/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/adapters/shared/*.rb

%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/connection_pool/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/plugins/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/model/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/database/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/adapters/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/extensions/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/dataset/*.rb


%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/CHANGELOG
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/MIT-LICENSE
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/doc/*.rdoc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/doc/release_notes/*.txt
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
