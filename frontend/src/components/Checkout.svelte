<script lang="ts">
  import type {
    CreateOrderActions,
    CreateOrderData,
    OnApproveActions,
    OnApproveData,
    OnCancelledActions,
  } from "@paypal/paypal-js";
  import PaypalButton from "./PaypalButton.svelte";

  export let paypalClientId: string;

  let info = "";
  let error = "";

  async function createOrder(
    data: CreateOrderData,
    actions: CreateOrderActions
  ) {
    info = "";
    error = "";
    const response = await fetch("/orders", {
      method: "POST",
      body: JSON.stringify({
        // TODO payload fields
      }),
    });
    const invoice = await response.json();
    if (response.ok) {
      return await actions.order.create(invoice);
    } else {
      throw new Error(invoice);
    }
  }
  async function onApprove(data: OnApproveData, actions: OnApproveActions) {
    const response = await fetch(`/orders/${data.orderID}/capture`, {
      method: "PUT",
      body: JSON.stringify({
        // TODO payload fields
      }),
    });
    const order = await response.json();
    if (response.ok) {
      info = "Order created!";
    } else {
      throw new Error(order);
    }
  }
  async function onCancel(
    data: Record<string, any>,
    actions: OnCancelledActions
  ) {}
  async function onError(e: Record<string, any>) {
    console.log(e);
    error = `Error: ${error}`;
  }
</script>

<form>
  {#if info}
    <div class="alert alert-info" role="alert">
      {info}
    </div>
  {/if}
  {#if error}
    <div class="alert alert-danger" role="alert">
      {error}
    </div>
  {/if}
  <!-- TODO payload fields -->
  <PaypalButton
    {paypalClientId}
    {createOrder}
    {onApprove}
    {onError}
    {onCancel}
  />
</form>
