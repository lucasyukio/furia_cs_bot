import requests

def get_proximo_jogo_furia():
    try:
        url = "https://hltv-api.vercel.app/api/matches.json"
        response = requests.get(url)
        response.raise_for_status()
        matches = response.json()

        for match in matches:
            teams_raw = match.get("teams", [])

            # Validação forte da estrutura
            if not isinstance(teams_raw, list) or len(teams_raw) != 2:
                continue

            team_names = []
            for team in teams_raw:
                if isinstance(team, dict) and "name" in team:
                    team_names.append(team["name"])
                else:
                    team_names.append("Desconhecido")

            if any(name.strip().upper() == "FURIA" for name in team_names):
                return (
                    f"🎯 Próximo jogo da FURIA:\n"
                    f"🆚 {team_names[0]} x {team_names[1]}\n"
                    f"🏆 Evento: {match.get('event', 'N/A')}\n"
                    f"📅 Data: {match.get('date', 'Data não disponível')}"
                )

        return "Nenhum jogo da FURIA encontrado nos próximos dias."

    except Exception as e:
        return f"Erro ao buscar dados: {e}"

def get_ranking_furia():
    # Dados simulados do ranking atual (abril 2025)
    # Você pode atualizar isso manualmente conforme quiser
    rank = 16
    pontos = 103

    return (
        f"📊 A FURIA está atualmente em **#{rank}** no ranking mundial da HLTV "
        f"com **{pontos} pontos**."
    )

