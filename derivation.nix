{ lib
, python3Packages
, google-chrome
, chromedriver
}:

with python3Packages;

buildPythonApplication {
  pname = "example-heroku-flask-selenium";
  version = "0.1.0.0";
  src = ./.;
  doCheck = false;

  postBuild = ''
    mkdir -p $out/bin
    ln -s ${google-chrome}/bin/google-chrome-stable $out/bin/google-chrome
  '';

  propagatedBuildInputs = [
    flask
    google-chrome
    chromedriver
    selenium
  ];
}
