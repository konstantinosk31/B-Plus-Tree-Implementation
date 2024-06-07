import ctypes
import streamlit as st

frontend = ctypes.CDLL("./backend.so")

def user_input():
    st.title("Perfect Weather Getaway")
    st.image('../assets/images/travelsmyth_logo.png')


    prompt = st.text_input("Enter your trip: ")
    st.markdown("<h4 style='text-align: center;'>Add more options for your trip</h4>", unsafe_allow_html=True)

    st.markdown("#### Select dates")
    date_of_arrival = st.date_input('Date of arrival')
    date_of_deperature = st.date_input('Date of departure')

    st.markdown("#### Select Country")
    countries = [(country.name, country.alpha_2) for country in pycountry.countries]
    selected_country = st.multiselect("Select a country", countries, format_func=lambda x: x[0])
    #print(selected_country)
    flag_urls = []
    for country in selected_country:
        flag_urls.append(get_flag_url(country[1]))
    st.write(
        " ".join([f"<img src='{url}' width='40' style='margin-right: 10px;'>" for url in flag_urls]), 
        unsafe_allow_html=True
    )
    
    st.markdown("#### Select Weather")
    weather = st.radio('Weather:', ['Sunny','Rainy','Snow'])
    min_temperature = st.number_input('Enter minimum temperature')
    max_temperature = st.number_input('Enter maximum temperature')
    
    st.markdown("#### Select Activities")
    categories = show_categories()
    
    if st.button('Search'):
        with st.spinner(text='In progress'):
            preferred_countries = ""
            for country in selected_country:
                preferred_countries += country[0]
                preferred_countries += ", "
            if len(preferred_countries) > 0:
                prompt += f"\n Countries that we prefer to go are {preferred_countries}. \n"
            prompt += "Use the following instructions when answering the prompt above: Reply in Json format Include the places suggestions in an array. Suggest as many as you can, preferably at least 10. When writing, the place name includes only the name, not the country, wider region or continent. If the prompt is appropriate for any of the following categories include the category in the json: Categories: infinity_pool,heated_pool,indoor_pool,rooftop_pool,wave_pool,children_pool,panoramic_view_pool,pool_swim_up_bar,pool_water_slide,pool_lap_lanes,water_park,lazy_river,private_pool,dog_play_area,dog_sitting,dogs_stay_free,outdoor_pool,health_and_safety,treehouse,haunted,overwater_bungalows,three_star,skyscraper,four_star,five_star,yoga,tennis,small,adult_only,gym,accessible,cheap,parking,business,free_wifi,pool,nightlife,romantic,dog_friendly,family,spa,casino,honeymoon,eco_friendly,beach,beachfront,ski,ski_in_ski_out,historic,unusual,vineyard,monastery,castle,golf,luxury,boutique,ev_charging,jacuzzi_hot_tub,fireplace,all_inclusive"
            results = get_answer(prompt, categories)
            scores = {}
            url = {}
            best_csv = {}
            points = [] 
            for x in results:
                points.append((x['latitude'], x['longitude']))
                current_csv = get_weather(x['latitude'], x['longitude'])
                current_csv = mean_implementation(current_csv)
                # youre ready to do the classification
                # user inputs are [weather, min_temp, max_temp, date_of_arrival, date_of_departure, selected_country]
                scores[x['name']] = assign_score(current_csv, weather, min_temperature, max_temperature, date_of_arrival, date_of_deperature)
                x['url'] += f"&checkin_day={date_of_arrival.day}&checkin_month={date_of_arrival.month}&checkin_year={date_of_arrival.year}&checkout_day={date_of_deperature.day}&checkout_month={date_of_deperature.month}&checkout_year={date_of_deperature.year}"
                url[x['name']] = x['url']
                best_csv[x['name']] = current_csv
            #st.write(weathers)
            #st.write(results)
            scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
            top_recommendation = next(iter(scores))
            create_map(points[0][0], points[0][1], points)
            typewriter(f"Top recommended destination is : {top_recommendation}", 10)
            for (index, x) in enumerate(scores):
                st.markdown(
                    f"""
                    - Recommendation {index + 1} is: {x} | [Link]({url[x]})
                    """
                    )
            st.session_state.recommented_url = url[top_recommendation]
            st.session_state.best_csv = best_csv[top_recommendation]
            st.success('Done')
        
if __name__ == "__main__":
    st.sidebar.header("Menu")
    st.sidebar.write("")
    if st.sidebar.button('Show results'):
        st.session_state.screen = "result"
    
    if st.sidebar.button('Team'):
        st.session_state.screen = "welcome_screen"
    if st.sidebar.button('User input'):
        st.session_state.screen = "user_input"
        
    #if st.sidebar.button('How it works?'):
    #    st.session_state.screen = "how_it_works" 
        
    best_recommended_csv = None
    if st.session_state.screen == "welcome_screen":
        show_team()
    if st.session_state.screen == "result":
        show_results()
    if st.session_state.screen == "user_input":
        best_recommended_csv = user_input()
        # histogram_plot(best_recommended_csv)
    #if st.session_state.screen == "how_it_works":
    #    how_it_works()
    if(st.session_state.best_csv.empty):
        pass
    else:
        histogram_plot(st.session_state.best_csv)
    #data = pd.read_csv("../api/data.csv")
    #fig = plot_weather_data(data, )
    #print(st.session_state.screen)


frontend.insert_and_export_dot_file(5)
frontend.insert_and_export_dot_file(6)
frontend.insert_and_export_dot_file(7)
frontend.insert_and_export_dot_file(8)
frontend.insert_and_export_dot_file(9)
frontend.insert_and_export_dot_file(10)
frontend.delete_and_export_dot_file(10)
print(frontend.search_and_export_bool(10))
print(frontend.search_and_export_bool(7))