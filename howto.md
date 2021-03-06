### gem, ruby and jekyll installation
    # sudo apt-get install ruby-full build-essential zlib1g-dev
    # echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
    # echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
    # echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
    # source ~/.bashrc
    # gem install jekyll bundler
    # gem install github-pages
    # bundle update
    # bundle install

### how to load the website
    # 1) go to website directory
    # 2) build site for internal developing: bundle exec jekyll serve --incremental --livereload

### in includes folder you can find default custom layouts for header, navbar and footer