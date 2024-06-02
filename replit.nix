{ pkgs }: {
  deps = [
    pkgs.mailutils
    pkgs.python39Packages.flask
  ];
}