{ pkgs, ... }:

{
  packages = with pkgs; [ streamlit ];
  languages.python = {
    enable = true;
    package = pkgs.python3.withPackages (p: with p; [
      spacy
      spacy_models.pt_core_news_md
    ]);
    poetry = {
      enable = true;
      activate.enable = true;
      install.enable = true;
    };
  };
}
