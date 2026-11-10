import streamlit as st
import app_db

st.title("STREAMLIT DATABASE UI")

option = st.sidebar.selectbox("Select Your Option:", (
                        "SELECT ALL RECORDS",
                        "SELECT RECORD BY ID",
                        "SELECT RECORD BY NAME",
                        "SELECT RECORD BY RATE",
                        "INSERT RECORD",
                        "DELETE RECORD BY ID",
                        "DELETE RECORD BY NAME",
                        "UPDATE RECORD BY ID",
                        "UPDATE RECORD BY NAME"))

# =========================
if option == "SELECT ALL RECORDS":
    if st.button("show data"):
        movies = app_db.select_all_records()

        for movie in movies:
            st.write(f"ID : {movie[0]}")
            st.write(f"Title : {movie[1]}")
            st.write(f"Year : {movie[2]}")
            st.write(f"Country : {movie[3]}")
            st.write(f"IMDB Rate : {movie[4]}")
            st.divider()

# =========================
elif option == "SELECT RECORD BY ID":
    movie_id = st.number_input("Enter Movie ID", min_value=1, step=1)

    if st.button("SEARCH"):
        movie = app_db.select_records_by_id(movie_id)

        if movie:
            st.write(f"ID : {movie[0]}")
            st.write(f"Title : {movie[1]}")
            st.write(f"Year : {movie[2]}")
            st.write(f"Country : {movie[3]}")
            st.write(f"IMDB Rate : {movie[4]}")
        else :
            st.warning("ID NOT EXISTS!")
# =========================
elif option == "SELECT RECORD BY NAME":
    movie_name = st.text_input("Enter Movie Name")

    if st.button("SEARCH"):
        movies = app_db.select_records_by_name(movie_name)

        if movies:
            for movie in movies:
                st.write(f"ID : {movie[0]}")
                st.write(f"Title : {movie[1]}")
                st.write(f"Year : {movie[2]}")
                st.write(f"Country : {movie[3]}")
                st.write(f"IMDB Rate : {movie[4]}")
                st.divider()
        else:
            st.warning("MOVIE NOT EXISTS!")

# =========================
elif option == "SELECT RECORD BY RATE":
    movie_rate = st.number_input("Enter Movie IMDB Rate", min_value=1.0, max_value=10.0)

    if st.button("SEARCH"):
        movies = app_db.select_records_by_rate(movie_rate)

        if movies:
            for movie in movies:
                st.write(f"ID : {movie[0]}")
                st.write(f"Title : {movie[1]}")
                st.write(f"Year : {movie[2]}")
                st.write(f"Country : {movie[3]}")
                st.write(f"IMDB Rate : {movie[4]}")
                st.divider()
        else:
            st.warning("MOVIE NOT EXISTS!")

# =========================
elif option == "INSERT RECORD":
    title = st.text_input("Enter Movie Title!")
    year = st.text_input("Enter Movie Year!")
    country = st.text_input("Enter Movie Country!")
    imdb_rate = st.number_input("Enter Movie IMDB Rate!", min_value=1.0, max_value=10.0)
    if st.button("SAVE"):
        if title != "" and year != "" and country != "" \
        and imdb_rate != "":
            app_db.insert_record(title, year, country, imdb_rate)
            st.success("SAVED SUCCESSFULLY")
        else:
            st.warning("FILL ALL BLANK!")

# =========================
elif option == "DELETE RECORD BY NAME":

    movie_name = st.text_input("Enter Movie Name")

    if st.button("DELETE"):

        movies = app_db.select_records_by_name(movie_name)

        if not movies:

            st.warning("MOVIE NOT EXISTS!")

        elif len(movies) == 1:

            result = app_db.delete_records_by_name(movie_name)

            if result:
                st.success("RECORD DELETED")

        else:

            st.session_state["delete_movies"] = movies


    if "delete_movies" in st.session_state:

        movies = st.session_state["delete_movies"]

        if movies:

            st.warning(f"{len(movies)} MOVIES FOUND!")

            for movie in movies:

                st.write(f"ID : {movie[0]}")
                st.write(f"Title : {movie[1]}")
                st.write(f"Year : {movie[2]}")
                st.write(f"Country : {movie[3]}")
                st.write(f"IMDB Rate : {movie[4]}")
                st.divider()


            movie_id = st.number_input(
                "Enter Movie ID To Delete",
                min_value=1,
                step=1
            )

            if st.button("DELETE SELECTED"):

                result = app_db.delete_records_by_id(movie_id)

                if result:

                    st.success("RECORD DELETED")

                    st.session_state["delete_movies"] = []

                else:

                    st.warning("ID NOT EXISTS!")

# =========================
elif option == "UPDATE RECORD BY ID":
    movie_id = st.number_input("Enter Movie ID", min_value=1, step=1)

    title = st.text_input("Enter New Movie Title")
    year = st.text_input("Enter New Movie Year")
    country = st.text_input("Enter New Movie Country")
    imdb_rate = st.number_input("Enter New Movie IMDB Rate", min_value=1.0, max_value=10.0)

    if st.button("UPDATE"):

        if title != "" and year != "" and country != "" and imdb_rate != "":
            
            result = app_db.update_records_by_id(
                movie_id,
                title,
                year,
                country,
                imdb_rate
            )

            if result:
                st.success("MOVIE UPDATED")
            else:
                st.warning("ID NOT EXISTS!")

        else:
            st.warning("FILL ALL BLANK!")


# =========================
elif option == "UPDATE RECORD BY NAME":
    movie_name = st.text_input("Enter Movie Name")
    year = st.text_input("Enter New Movie Year")
    country = st.text_input("Enter New Movie Country")
    imdb_rate = st.number_input("Enter New Movie IMDB Rate", min_value=1.0, max_value=10.0)

    if st.button("UPDATE"):

        if movie_name != "" and year != "" and country != "" and imdb_rate != "":
            result = app_db.update_records_by_name(
                movie_name,
                year,
                country,
                imdb_rate
            )

            if result:
                st.success("MOVIE UPDATED")
            else:
                st.warning("MOVIE NOT EXISTS!")
        else:
            st.warning("FILL ALL BLANK!")