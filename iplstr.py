import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
# streamlit run iplstr.py 
# Load Data
df = pd.read_csv("IPL.csv", low_memory=False)
df["date"] = pd.to_datetime(df["date"])
df["season"] = df["date"].dt.year

st.sidebar.title("🏆 IPL Cricket Analytics Dashboard")
home = st.sidebar.radio(
    "Select a page",
    ["🏠Home", "👥 Team Comparison", "👤 Player Stats","📈 Points Table", "📊 Analytics"]
)


# HOME PAGE

if home == "🏠Home":

    st.title("🏆 IPL Cricket Analytics Dashboard")
    st.markdown("### Your comprehensive guide to IPL statistics and insights")
    st.markdown("---")

    all_seasons = sorted(df["season"].unique())
    selected_season = st.selectbox("🏳️ Select Season", all_seasons, key="home_season")

    current_ = df[df["season"] == selected_season]
    season_teams = sorted(
        pd.concat([current_["batting_team"], current_["bowling_team"]])
        .dropna().unique()
    )
    season_df = df[df["season"] <= selected_season]

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🏏🧤 Select Team 1")
        team1 = st.selectbox("Choose first team", season_teams, index=0, key="team1")
    with col2:
        st.subheader("🏏🧤 Select Team 2")
        team2_options = [t for t in season_teams if t != team1]
        team2 = st.selectbox("Choose second team", team2_options, index=0, key="team2")

    st.session_state["selected_team1"] = team1
    st.session_state["selected_team2"] = team2
    st.session_state["selected_season"] = selected_season

    st.markdown("---")

    h2h = df[
        (
            ((df["batting_team"] == team1) &
            (df["bowling_team"] == team2))
            |
            ((df["batting_team"] == team2) &
            (df["bowling_team"] == team1))
        )
    ]

    total_matches = h2h["match_id"].nunique()
    team1_wins = h2h[h2h["match_won_by"] == team1]["match_id"].nunique()
    team2_wins = h2h[h2h["match_won_by"] == team2]["match_id"].nunique()
    no_result = total_matches - team1_wins - team2_wins

    st.success(f"### 🤝 Head to Head: {team1} vs {team2}")
    st.markdown(f"**2007 thi {selected_season} sudha na matches**")

    col3, col4, col5, col6 = st.columns(4)
    with col3:
        st.metric("Total Matches", total_matches)
    with col4:
        st.metric(f"{team1} Wins", team1_wins)
    with col5:
        st.metric(f"{team2} Wins", team2_wins)
    with col6:
        st.metric("No Result / Ties", no_result)

    st.markdown("---")
    st.title("🧍 Playing XI comparison between Teams ")
    st.markdown("---")

    tab1, tab2 = st.tabs([f"🏏 {team1}", f"🏏 {team2}"])

    # ── Team 1
    with tab1:
        t1_df = current_[
            (current_["batting_team"] == team1) |
            (current_["bowling_team"] == team1)
        ]
        t1_batters = set(t1_df[t1_df["batting_team"] == team1]["batter"].dropna().unique())
        t1_bowlers = set(t1_df[t1_df["bowling_team"] == team1]["bowler"].dropna().unique())
        t1_players = t1_batters.union(t1_bowlers)

        st.markdown(f"### 🏏 {team1} - All Players ({selected_season})")
        st.markdown(f"**Total Players: {len(t1_players)}**")
        st.markdown("---")

        for i, player in enumerate(sorted(t1_players), 1):
            is_batter = player in t1_batters
            is_bowler = player in t1_bowlers
            if is_batter and is_bowler:
                role = "⚡ All-Rounder"
            elif is_batter:
                role = "🏏 Batter"
            else:
                role = "⚾ Bowler"
            col_a, col_b, col_c = st.columns([1, 3, 2])
            with col_a:
                st.markdown(f"**#{i}**")
            with col_b:
                st.markdown(f"**{player}**")
            with col_c:
                st.markdown(f"{role}")
            st.markdown("---")

    # ── Team 2
    with tab2:
        t2_df = current_[
            (current_["batting_team"] == team2) |
            (current_["bowling_team"] == team2)
        ]
        t2_batters = set(t2_df[t2_df["batting_team"] == team2]["batter"].dropna().unique())
        t2_bowlers = set(t2_df[t2_df["bowling_team"] == team2]["bowler"].dropna().unique())
        t2_players = t2_batters.union(t2_bowlers)

        st.markdown(f"### 🏏 {team2} - All Players ({selected_season})")
        st.markdown(f"**Total Players: {len(t2_players)}**")
        st.markdown("---")

        for i, player in enumerate(sorted(t2_players), 1):
            is_batter = player in t2_batters
            is_bowler = player in t2_bowlers
            if is_batter and is_bowler:
                role = "⚡ All-Rounder"
            elif is_batter:
                role = "🏏 Batter"
            else:
                role = "⚾ Bowler"
            col_a, col_b, col_c = st.columns([1, 3, 2])
            with col_a:
                st.markdown(f"**#{i}**")
            with col_b:
                st.markdown(f"**{player}**")
            with col_c:
                st.markdown(f"{role}")
            st.markdown("---")




# TEAM COMPARISON PAGE

elif home == "👥 Team Comparison":

    if "selected_team1" not in st.session_state:
        st.warning("⚠️ First select teams from Home page.")
        st.stop()

    team1 = st.session_state["selected_team1"]
    team2 = st.session_state["selected_team2"]
   
    st.title("🏏 Team Comparison")
    st.markdown(f"🤜🤛 {team1} vs {team2}")
    st.write(f"🔰 2008 to 2025 all seasons included")
    st.markdown("---")

    team_stats = {}

    for t in [team1, team2]:

        team_matches = df[
            (df["batting_team"] == t) |
            (df["bowling_team"] == t)
        ]

        total_matches = team_matches["match_id"].nunique()

        wins = team_matches[
            team_matches["match_won_by"] == t
        ]["match_id"].nunique()

        losses = total_matches - wins

        batting_df = team_matches[
            team_matches["batting_team"] == t
        ]

        total_runs = batting_df["runs_total"].sum()

        total_balls = batting_df["valid_ball"].sum()

        run_rate = round(
            total_runs / (total_balls / 6), 2
        ) if total_balls > 0 else 0

        bowling_df = team_matches[
            team_matches["bowling_team"] == t
        ]

        total_wickets = bowling_df["bowler_wicket"].sum()

        runs_conceded = bowling_df["runs_total"].sum()

        balls_bowled = bowling_df["valid_ball"].sum()

        economy = round(
            runs_conceded / (balls_bowled / 6), 2
        ) if balls_bowled > 0 else 0

        team_stats[t] = {
            "matches": total_matches,
            "wins": wins,
            "losses": losses,
            "win_pct": round(
                (wins / total_matches) * 100, 2
            ) if total_matches > 0 else 0,
            "runs": total_runs,
            "run_rate": run_rate,
            "wickets": total_wickets,
            "economy": economy
        }

    s1 = team_stats[team1]
    s2 = team_stats[team2]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"🤜 {team1}")
        st.metric("Matches", s1["matches"])
        st.metric("Wins", s1["wins"])
        st.metric("Losses", s1["losses"])
        st.metric("Win %", f"{s1['win_pct']}%")
        st.metric("Runs Scored", int(s1["runs"]))
        st.metric("Run Rate", s1["run_rate"])
        st.metric("Wickets", int(s1["wickets"]))
        st.metric("Economy", s1["economy"])

    with col2:
        st.subheader(f"🤛 {team2}")
        st.metric("Matches", s2["matches"])
        st.metric("Wins", s2["wins"])
        st.metric("Losses", s2["losses"])
        st.metric("Win %", f"{s2['win_pct']}%")
        st.metric("Runs Scored", int(s2["runs"]))
        st.metric("Run Rate", s2["run_rate"])
        st.metric("Wickets", int(s2["wickets"]))
        st.metric("Economy", s2["economy"])

    st.markdown("---")

    h2h = df[
        (
            ((df["batting_team"] == team1) &
             (df["bowling_team"] == team2))
            |
            ((df["batting_team"] == team2) &
             (df["bowling_team"] == team1))
        )
    ]

    total_h2h = h2h["match_id"].nunique()

    team1_h2h_wins = h2h[
        h2h["match_won_by"] == team1
    ]["match_id"].nunique()

    team2_h2h_wins = h2h[
        h2h["match_won_by"] == team2
    ]["match_id"].nunique()

    st.subheader("🤝 Head-to-Head Record")

    h1, h2, h3 = st.columns(3)

    h1.metric("Matches", total_h2h)
    h2.metric(f"{team1} Wins", team1_h2h_wins)
    h3.metric(f"{team2} Wins", team2_h2h_wins)

    st.markdown("---")

    st.subheader("📊 Win Percentage Comparison")

    win_df = pd.DataFrame({
        "Team": [team1, team2],
        "Win %": [s1["win_pct"], s2["win_pct"]]
    }).set_index("Team")

    st.bar_chart(win_df)

    st.subheader("🏃‍♂️ Total Runs Comparison")

    runs_df = pd.DataFrame({
        "Team": [team1, team2],
        "Runs": [s1["runs"], s2["runs"]]
    }).set_index("Team")

    st.bar_chart(runs_df)

    st.subheader("⚾ Wickets Comparison")

    wickets_df = pd.DataFrame({
        "Team": [team1, team2],
        "Wickets": [s1["wickets"], s2["wickets"]]
    }).set_index("Team")

    st.bar_chart(wickets_df)

elif home == "👤 Player Stats":
    st.title("🏏 Player Stats")
    st.markdown("---")

    all_batters = set(df["batter"].dropna().unique())
    all_bowlers = set(df["bowler"].dropna().unique())
    all_players = sorted(all_batters.union(all_bowlers))

    selected_player = st.selectbox(
        "🔍 Search Player",
        all_players,
        index=None,
        placeholder="Type player name...",
        key="ps_player"
    )

    st.markdown("---")

    is_batter = selected_player in all_batters
    is_bowler = selected_player in all_bowlers

    if is_batter and is_bowler:
        role = "⚡ All-Rounder"
    elif is_batter:
        role = "🏏 Batter"
    else:
        role = "🎯 Bowler"

    st.markdown(f"### ⏩ {selected_player} — {role}")
    st.markdown("---")

    # total team of player

    player_teams = set(df[df["batter"] == selected_player]["batting_team"].dropna().unique())
    player_teams = player_teams.union(set(df[df["bowler"] == selected_player]["bowling_team"].dropna().unique()))

    st.markdown(f"**ToTal Teams: {len(player_teams)}**\nTeam names: {player_teams}")

    st.markdown("---")


    if is_batter:

        st.title("🏏 Batting Career Stats")

        bat_df = df[df["batter"] == selected_player]

        # Matches
        career_matches = bat_df["match_id"].nunique()

        # Runs
        career_runs = bat_df["runs_batter"].sum()

        # Balls Faced
        career_balls = bat_df["valid_ball"].sum()

        # Strike Rate
        strike_rate = round(
            (career_runs / career_balls) * 100, 2
        ) if career_balls > 0 else 0

        # Highest Score
        per_match_runs = bat_df.groupby("match_id")["runs_batter"].sum()

        highest_score = (
            per_match_runs.max()
            if not per_match_runs.empty
            else 0
        )

        # Boundaries
        fours = (bat_df["runs_batter"] == 4).sum()
        sixes = (bat_df["runs_batter"] == 6).sum()

        # 50s & 100s
        fifties = (
            (per_match_runs >= 50) &
            (per_match_runs < 100)
        ).sum()

        hundreds = (
            per_match_runs >= 100
        ).sum()

        bc1, bc2, bc3, bc4 = st.columns(4)

        bc1.metric("Matches", career_matches)
        bc2.metric("Runs", int(career_runs))
        bc3.metric("Balls Faced", int(career_balls))
        bc4.metric("Strike Rate", strike_rate)

        bc5, bc6, bc7, bc8 = st.columns(4)

        bc5.metric("Highest Score", int(highest_score))
        bc6.metric("4s", int(fours))
        bc7.metric("6s", int(sixes))
        bc8.metric("50s / 100s", f"{fifties} / {hundreds}")

        
        st.markdown("---")
        player_df = df[df["batter"] == selected_player]
        st.subheader("🖐 Batting Stats")
        st.dataframe(player_df)
        st.markdown("---")
        st.title("Runs by Season garph")

        season_runs = bat_df.groupby("season")["runs_batter"].sum()
        st.markdown("🎰 Runs by Season")
        st.bar_chart(season_runs)

        st.markdown("---")

    if is_bowler:

        st.title("🎯 Bowling Career Stats")

        bowl_df = df[df["bowler"] == selected_player]

        matches = bowl_df["match_id"].nunique()

        wickets = bowl_df["bowler_wicket"].sum()

        balls_bowled = bowl_df["valid_ball"].sum()

        runs_conceded = bowl_df["runs_total"].sum()

        overs = round(balls_bowled / 6, 1)

        economy = round(
            runs_conceded / (balls_bowled / 6), 2
        ) if balls_bowled > 0 else 0

        best_figures = (
            bowl_df.groupby("match_id")["bowler_wicket"].sum().max()
            if not bowl_df.groupby("match_id")["bowler_wicket"].sum().empty
            else 0
        )

        c1, c2, c3, c4, c5,c6 = st.columns(6)

        c1.metric("Matches", matches)
        c2.metric("Wickets", int(wickets))
        c3.metric("Balls", int(balls_bowled))
        c4.metric("Overs", overs)
        c5.metric("Economy", economy)
        c6.metric("Best (Wkts in Match)", int(best_figures))

        st.markdown("---")
        player_df = df[df["bowler"] == selected_player]
        st.subheader("⛹ Bowling Stats")
        st.dataframe(player_df)

        st.markdown("---")

        st.markdown("🏃 Runs by Season")
        season_wickets = bowl_df.groupby("season")["bowler_wicket"].sum()
        st.markdown("##### Wickets by Season")
        st.bar_chart(season_wickets)

        st.markdown("---")
        st.info("🏅 Orange Cap & Purple Cap Leaderboards")

        st.markdown("---")

        all_seasons = sorted(df["season"].unique())
        selected_season = st.selectbox("Select Season", all_seasons, key="home_season")
        st.markdown("---")
        tab1, tab2 = st.tabs(["🟠 Orange Cap", "🟣 Purple Cap"])

        with tab1:
            st.markdown("🟠 Orange Cap (Most Runs)")

            orange_cap_df = df[df["season"] == selected_season]
            orange_cap_df = orange_cap_df.groupby("batter")["runs_batter"].sum().reset_index()
            orange_cap_df = orange_cap_df.sort_values("runs_batter", ascending=False).head(10)
            st.dataframe(orange_cap_df)

            # plotly_chart(orange_cap_df, "Runs", "Player") Horizontal Bar Charts

            st.markdown("---")
            fig = px.bar(
                orange_cap_df,
                x="runs_batter",
                y="batter",
                orientation="h",
                title="🟠 Orange Cap (Most Runs)",
                template="plotly_white",
                color_discrete_sequence=["#FF5E0E"],    
            )
            st.plotly_chart(
                fig, use_container_width=True
            )

            st.markdown("---")


        with tab2:
            st.markdown("🟣 Purple Cap (Most Wickets)")

            purple_cap_df = df[df["season"] == selected_season]
            purple_cap_df = purple_cap_df.groupby("bowler")["bowler_wicket"].sum().reset_index()
            purple_cap_df = purple_cap_df.sort_values("bowler_wicket", ascending=False).head(10)
            st.dataframe(purple_cap_df)

            # plotly_chart(purple_cap_df, "Wickets", "Player") Horizontal Bar Charts

            st.markdown("---")
            fig = px.bar(
                purple_cap_df,
                x="bowler_wicket",
                y="bowler",
                orientation="h",
                title="🟣 Purple Cap (Most Wickets)",
                template="plotly_white",
                color_discrete_sequence=["#6A0DAD"],
            )
            st.plotly_chart(
                fig, use_container_width=True
            )

            st.markdown("---")

elif home == "📈 Points Table":
    st.title("📈 Points Table")
    st.markdown("---")
    all_seasons = sorted(df["season"].unique())
    selected_season = st.selectbox("Select Season", all_seasons, key="home_season")

    st.success(f"🏆 Standings -- {selected_season}")

    st.markdown("---")
    season_df = df[df["season"] == selected_season]

    teams = sorted(
        pd.concat([
            season_df["batting_team"],
            season_df["bowling_team"]
        ]).dropna().unique()
    )

    points_table = []

    for team in teams:

        matches = season_df[
            (season_df["batting_team"] == team) |
            (season_df["bowling_team"] == team)
        ]["match_id"].nunique()

        wins = season_df[
            season_df["match_won_by"] == team
        ]["match_id"].nunique()

        losses = matches - wins

        runs_scored = season_df[
            season_df["batting_team"] == team
        ]["runs_total"].sum()

        runs_conceded = season_df[
            season_df["bowling_team"] == team
        ]["runs_total"].sum()

        balls_faced = season_df[
            season_df["batting_team"] == team
        ]["valid_ball"].sum()

        balls_bowled = season_df[
            season_df["bowling_team"] == team
        ]["valid_ball"].sum()

        nrr = 0

        if balls_faced > 0 and balls_bowled > 0:
            team_rr = runs_scored / (balls_faced / 6)
            opp_rr = runs_conceded / (balls_bowled / 6)
            nrr = round(team_rr - opp_rr, 3)

        points = wins * 2

        points_table.append([
            team,
            matches,
            wins,
            losses,
            points,
            nrr
        ])
    points_df = pd.DataFrame(
        points_table,
        columns=[
            "Team",
            "Matches",
            "Wins",
            "Losses",
            "Points",
            "NRR"
        ]
    )

    points_df = points_df.sort_values(
        ["Points", "NRR"],
        ascending=False
    ).reset_index(drop=True)

    points_df.index += 1

    st.dataframe(
        points_df,
        use_container_width=True
    )

    st.markdown("---")

    fig = px.bar(
        points_df,
        x="Team",
        y="Points",
        color="Team",
        title=f"IPL {selected_season} Points Table"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")
    # net run rate
    fig = px.bar(
        points_df,
        x="Team",
        y="NRR",
        color="NRR",
        title=f"IPL {selected_season} Net Run Rate"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")
elif home == "📊 Analytics":

    st.title("📊 Analytics")
    st.markdown("---")

    st.subheader("🏏 Total Runs by Season")

    season_runs = (
        df.groupby("season")["runs_total"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        season_runs,
        x="season",
        y="runs_total",
        markers=True,
        title="Total Runs by Season"
    )
    fig.update_traces(
        line=dict(color="#C94949", width=3),
        marker=dict(size=8, color="#84721A")
    )

    fig.update_layout(
        xaxis_title="Season",
        yaxis_title="Runs",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.subheader("🏏 Total Wickets by Season")

    season_wickets = (
        df.groupby("season")["bowler_wicket"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        season_wickets,
        x="season",
        y="bowler_wicket",
        markers=True,
        title="Total Wickets by Season"
    )

    fig.update_traces(
        line=dict(color="#13BB7D", width=3),
        marker=dict(size=8, color="#3E4275")
    )

    fig.update_layout(
        xaxis_title="Season",
        yaxis_title="Wickets",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)  

    st.subheader("🏏 Team Wise Total Runs (2008-2025)")

    team_runs = (
        df.groupby("batting_team")["runs_total"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        team_runs,
        x="batting_team",
        y="runs_total",
        color="runs_total",
        color_continuous_scale="Oranges",
        title="Total Runs Scored By Teams"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🎯 Team Wise Total Wickets (2008-2025)")

    team_wickets = (
        df.groupby("bowling_team")["bowler_wicket"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        team_wickets,
        x="bowling_team",
        y="bowler_wicket",
        color="bowler_wicket",
        color_continuous_scale="Purples",
        title="Total Wickets Taken By Teams"
    )

    st.plotly_chart(fig, use_container_width=True)

    top_run_team = team_runs.iloc[0]
    top_wicket_team = team_wickets.iloc[0]

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "🏏 Most Runs Team",
            top_run_team["batting_team"],
            f"{int(top_run_team['runs_total'])} Runs"
        )

    with c2:
        st.metric(
            "🎯 Most Wickets Team",
            top_wicket_team["bowling_team"],
            f"{int(top_wicket_team['bowler_wicket'])} Wickets"
        )