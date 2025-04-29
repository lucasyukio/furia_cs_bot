import requests

def get_proximo_jogo_furia():
    try:
        url = "https://hltv-api.vercel.app/api/matches.json"
        response = requests.get(url)
        response.raise_for_status()
        matches = response.json()

        jogos_futuros_furia = []

        for match in matches:
            teams_raw = match.get("teams", [])
            event_data = match.get("event", {})
            event_name = event_data.get("name", "").lower()

            # Pular eventos da academy
            if "academy" in event_name:
                continue

            # Verificação básica da estrutura dos times
            if not isinstance(teams_raw, list) or len(teams_raw) != 2:
                continue

            team_names = []
            for team in teams_raw:
                if isinstance(team, dict) and "name" in team:
                    team_names.append(team["name"])
                else:
                    team_names.append("Desconhecido")

            # Se FURIA for um dos dois times e não for FURIA Academy
            if any(name.upper() == "FURIA" for name in team_names) and all("academy" not in name.lower() for name in team_names):
                jogos_futuros_furia.append({
                    "teams": team_names,
                    "event": event_data.get("name", "N/A"),
                    "date": match.get("date", "Data não disponível")
                })

        if jogos_futuros_furia:
            jogo = jogos_futuros_furia[0]
            return (
                f"🎯 Próximo jogo da FURIA:\n"
                f"🆚 {jogo['teams'][0]} x {jogo['teams'][1]}\n"
                f"🏆 Evento: {jogo['event']}\n"
                f"📅 Data: {jogo['date']}"
            )
        else:
            return "⚠️ Nenhum jogo futuro da FURIA principal encontrado."

    except Exception as e:
        return f"❌ Erro ao buscar dados: {e}"

def get_ranking_furia():
    rank = 16
    pontos = 103

    return (
        f"📊 A FURIA está atualmente em **#{rank}** no ranking mundial da HLTV "
        f"com **{pontos} pontos**."
    )