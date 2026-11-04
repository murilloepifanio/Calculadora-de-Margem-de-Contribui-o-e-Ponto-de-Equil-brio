"""Calculadora de margem de contribuição e ponto de equilíbrio.

Autor: Murillo Epifânio Rodrigues de Almeida.
Projeto educacional de análise financeira para pequenos negócios.
"""

import math


def calcular_indicadores(preco, custo_variavel_unid, despesas_fixas, quantidade_vendida):
    """Calcula indicadores financeiros a partir dos dados informados.

    Args:
        preco (float): Preço de venda por unidade, em reais.
        custo_variavel_unid (float): Custo/despesa variável por unidade, em reais.
        despesas_fixas (float): Despesas fixas do período, em reais.
        quantidade_vendida (int): Número de unidades vendidas no período.

    Returns:
        dict: Margem unitária, ponto de equilíbrio, receita, custos e resultado.

    Raises:
        ValueError: Se os valores forem inválidos ou a margem não for positiva.
    """
    if preco <= 0:
        raise ValueError("O preço deve ser maior que zero.")
    if custo_variavel_unid < 0 or despesas_fixas < 0:
        raise ValueError("Custos e despesas não podem ser negativos.")
    if not isinstance(quantidade_vendida, int) or quantidade_vendida < 0:
        raise ValueError("A quantidade deve ser um número inteiro não negativo.")

    # Cada unidade contribui para cobrir despesas fixas e gerar resultado.
    margem_unitaria = preco - custo_variavel_unid
    if margem_unitaria <= 0:
        raise ValueError("Margem não positiva: reveja o preço e os custos.")

    # Arredonda para cima, pois não é possível vender fração de unidade.
    ponto_equilibrio = math.ceil(despesas_fixas / margem_unitaria)

    receita_total = quantidade_vendida * preco
    custo_variavel_total = quantidade_vendida * custo_variavel_unid
    resultado = receita_total - custo_variavel_total - despesas_fixas

    return {
        "margem_unitaria": margem_unitaria,
        "ponto_equilibrio": ponto_equilibrio,
        "receita_total": receita_total,
        "custo_variavel_total": custo_variavel_total,
        "resultado_simplificado": resultado,
    }


def ler_valor_monetario(mensagem):
    """Lê um valor monetário não negativo, aceitando vírgula decimal."""
    while True:
        try:
            valor = float(input(mensagem).strip().replace(",", "."))
            if not math.isfinite(valor) or valor < 0:
                raise ValueError
            return valor
        except ValueError:
            print("Digite um valor válido, maior ou igual a zero.")


def ler_quantidade(mensagem):
    """Lê uma quantidade inteira não negativa."""
    while True:
        entrada = input(mensagem).strip()
        try:
            quantidade = int(entrada)
            if quantidade < 0:
                raise ValueError
            return quantidade
        except ValueError:
            print("Digite um número inteiro não negativo.")


def calcula_resultados():
    """Solicita os dados ao usuário e apresenta o relatório simplificado."""
    print("=== CALCULADORA DE MARGEM E PONTO DE EQUILÍBRIO ===")

    preco = ler_valor_monetario("Preço de venda por unidade (R$): ")
    custo_variavel_unid = ler_valor_monetario("Custo variável por unidade (R$): ")
    despesas_fixas = ler_valor_monetario("Despesas fixas do mês (R$): ")
    quantidade_vendida = ler_quantidade("Quantidade vendida no mês: ")

    try:
        indicadores = calcular_indicadores(
            preco, custo_variavel_unid, despesas_fixas, quantidade_vendida
        )
    except ValueError as erro:
        print(f"Erro: {erro}")
        return

    print("\n=== RESULTADO ===")
    print(f"Margem de contribuição unitária: R$ {indicadores['margem_unitaria']:.2f}")
    print(f"Ponto de equilíbrio: {indicadores['ponto_equilibrio']} unidades")
    print(f"Receita total: R$ {indicadores['receita_total']:.2f}")
    print(f"Custos variáveis totais: R$ {indicadores['custo_variavel_total']:.2f}")
    print(f"Resultado simplificado: R$ {indicadores['resultado_simplificado']:.2f}")
    print("\nObservação: o resultado não é necessariamente o lucro líquido.")
    print("Inclua todos os tributos, custos e despesas aplicáveis na análise real.")


if __name__ == "__main__":
    calcula_resultados()
