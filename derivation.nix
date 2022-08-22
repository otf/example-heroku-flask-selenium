{ lib
, python3Packages
}:

with python3Packages;

buildPythonApplication {
  pname = "example-heroku-flask-selenium";
  version = "0.1.0.0";
  src = ./.;
  doCheck = false;

  propagatedBuildInputs = [
    flask
    selenium
  ];
}
