from livereload import Server


def make_site():
    # TODO convert markdown to html, create site
    print(1)


if __name__ == "__main__":
    server = Server()
    server.watch("templates/*.html", make_site)
    # TODO watch for changes in markdown articles
server.serve(root="site/")  # folder to serve html files from

