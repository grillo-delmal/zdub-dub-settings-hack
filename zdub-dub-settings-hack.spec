Name:           zdub-dub-settings-hack
Version:        0.1.0
Release:        %autorelease
Summary:        A shitty hack to make dub packages ... packageable

License:        MIT
URL:            https://github.com/grillo-delmal/zdub-dub-settings-hack
Source0:        https://github.com/grillo-delmal/zdub-dub-settings-hack/archive/%{version}/%{name}-%{version}.tar.gz

Requires:       dub

BuildArch:      noarch

%description
Adds a configuration file to trick dub into search for installed libraries
on the /usr/include/zdub path, at least until there is an actual way to do it.

%prep
%setup -q

%build

%install

mkdir -p %{buildroot}/%{_var}/lib/dub

install -m 0644 settings.json %{buildroot}/%{_var}/lib/dub/settings.json

%files
%license LICENSE
%{_var}/lib/dub/settings.json

%changelog
%autochangelog
