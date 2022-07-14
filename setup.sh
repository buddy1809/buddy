mkdir -p ~/.streamlit/

echo "\
[server]\n\
headlesss = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
