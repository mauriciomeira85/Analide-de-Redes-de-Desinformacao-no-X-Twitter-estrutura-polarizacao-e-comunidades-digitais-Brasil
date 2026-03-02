# analise-redes-desinformacao-x

Projeto Python para coleta, construção, análise e visualização de redes de interação no X (Twitter), com foco em investigação de possíveis dinâmicas de desinformação.

## Objetivos

- Coletar dados de posts/interações por múltiplas fontes (API, sessão/cookies, CSV offline)
- Construir grafos de **retweets** e **menções**
- Calcular métricas de centralidade e comunidades
- Exportar resultados reproduzíveis (CSV/Parquet, GEXF, PNG)
- Gerar relatório resumido automaticamente

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Estrutura

- `src/ardx/cli.py`: CLI principal
- `src/ardx/collectors/`: coletores
- `src/ardx/pipeline/`: etapas do pipeline
- `src/ardx/analysis/`: funções de análise de rede
- `configs/config.example.yaml`: configuração de exemplo
- `notebooks/`: espaço para exploração
- `tests/`: testes unitários

## Uso rápido

```bash
cd analise-redes-desinformacao-x
ardx collect --config configs/config.example.yaml
ardx build-network --config configs/config.example.yaml
ardx analyze --config configs/config.example.yaml
ardx visualize --config configs/config.example.yaml
ardx report --config configs/config.example.yaml
```

Ou rodar tudo:

```bash
ardx run-all --config configs/config.example.yaml
```

## Fontes de coleta

1. **x_api_collector.py** (Tweepy v2)
   - Usa variáveis de ambiente (placeholders):
     - `X_BEARER_TOKEN`
     - `X_API_KEY`
     - `X_API_SECRET`
     - `X_ACCESS_TOKEN`
     - `X_ACCESS_SECRET`
2. **twikit_collector.py**
   - Baseado em sessão/cookies (placeholder)
   - Possui tratamento robusto de erros e mensagens claras
3. **csv_collector.py**
   - Operação offline via CSV local (ideal para testes/reprodução)

## Ética e limitações

- Respeite Termos de Uso da plataforma e leis aplicáveis (LGPD etc.)
- Evite coleta de dados sensíveis desnecessários
- Minimizar risco de dano aos indivíduos analisados
- Resultados de centralidade/comunidade **não provam causalidade**
- Inclua revisão humana antes de qualquer conclusão pública

## Reprodutibilidade

- Configuração centralizada em YAML
- Exportação de artefatos intermediários/finais em formatos abertos
- Testes automatizados para funções centrais de grafo
- Possibilidade de execução offline sem credenciais reais

## Desenvolvimento e testes

```bash
pytest
```

## Próximos passos sugeridos

- Adicionar inferência temporal de cascatas
- Enriquecer visualizações com layout e filtros por comunidade
- Integrar geração de relatório em HTML/PDF
