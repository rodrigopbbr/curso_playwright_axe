def assert_sem_violacoes_graves(
    resultado: dict,
    severidades: tuple[str, ...] = ("critical", "serious"),
) -> None:
    violacoes = resultado["violations"]
    graves = [v for v in violacoes if v["impact"] in severidades]
    if not graves:
        return
    detalhes = "\n".join(
        f"- [{v['impact']}] {v['id']}: {len(v['nodes'])} elemento(s) afetado(s)"
        for v in violacoes
    )
    assert not graves, f"{len(violacoes)} violacao(oes) encontrada(s), {len(graves)} grave(s):\n{detalhes}"